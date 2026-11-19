"""
Kelir Senja - Horror Visual & Animation Frame Rendering Engine
Developer: Wanz
Gaya: Siluet Hitam Pekat x Pencahayaan Warm Amber Chiaroscuro x Horor Folklor Nusantara
"""

import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess
import os
import sys

def get_font(size=42):
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

class KelirSenjaRenderer:
    def __init__(self, width=1080, height=1920, fps=30):
        self.width = width
        self.height = height
        self.fps = fps
        self.font_sub = get_font(int(height * 0.024))
        self.font_sub_sm = get_font(int(height * 0.020))

    def create_radial_gradient(self, cx, cy, radius, inner_color, outer_color):
        """Buat gradasi radial pencahayaan api lentera warm amber."""
        Y, X = np.ogrid[:self.height, :self.width]
        dist_from_center = np.sqrt((X - cx)**2 + (Y - cy)**2)
        norm_dist = np.clip(dist_from_center / radius, 0.0, 1.0)
        
        # Kurva falloff kuadratik halus untuk cahaya lilin/lampu minyak
        falloff = (1.0 - norm_dist**1.4)[:, :, np.newaxis]
        falloff = np.clip(falloff, 0.0, 1.0)
        
        inner = np.array(inner_color, dtype=np.float32)
        outer = np.array(outer_color, dtype=np.float32)
        
        rgb = outer + (inner - outer) * falloff
        return np.clip(rgb, 0, 255).astype(np.uint8)

    def draw_gedhek_texture(self, draw, width, height, light_cx, light_cy, flicker_val):
        """Gambar dinding anyaman bambu (gedhek) dengan celah berkas cahaya temaram."""
        spacing = 38
        # Garis horizontal anyaman
        for y in range(0, int(height * 0.75), spacing):
            intensity = int(12 + 6 * math.sin(y * 0.05 + flicker_val))
            draw.line([(0, y), (width, y)], fill=(intensity, int(intensity*0.7), int(intensity*0.4)), width=2)
            
        # Garis vertikal anyaman
        for x in range(0, width, spacing):
            intensity = int(10 + 5 * math.cos(x * 0.04 + flicker_val))
            draw.line([(x, 0), (x, int(height * 0.75))], fill=(intensity, int(intensity*0.7), int(intensity*0.4)), width=2)
            
        # Berkas cahaya menembus celah bambu (light leaks)
        for i, (bx, by) in enumerate([(int(width*0.25), int(height*0.35)), 
                                      (int(width*0.72), int(height*0.28)), 
                                      (int(width*0.48), int(height*0.42))]):
            beam_alpha = int(45 + 30 * math.sin(flicker_val * 3.5 + i))
            draw.ellipse([bx-4, by-3, bx+4, by+3], fill=(255, 175, 50, beam_alpha))

    def draw_floor(self, draw, width, height):
        """Gambar lantai tanah liat pedesaan."""
        horizon_y = int(height * 0.72)
        draw.rectangle([0, horizon_y, width, height], fill=(14, 11, 9))
        for line_y in range(horizon_y, height, 40):
            prog = (line_y - horizon_y) / (height - horizon_y)
            c = int(18 + 12 * prog)
            draw.line([(0, line_y), (width, line_y)], fill=(c, int(c*0.8), int(c*0.6)), width=1)

    def draw_fog_layer(self, draw, width, height, frame_num, layer_offset=0):
        """Gambar kabut merayap di permukaan lantai tanah."""
        base_y = int(height * 0.70) + layer_offset
        points = [(0, height)]
        step = 40
        for x in range(0, width + step, step):
            wave = math.sin((x * 0.012) + (frame_num * 0.05) + layer_offset) * 25
            wave += math.cos((x * 0.025) - (frame_num * 0.03)) * 12
            y = base_y + wave
            points.append((x, y))
        points.append((width, height))
        draw.polygon(points, fill=(18, 22, 28, 45))

    def draw_bale_bambu(self, draw, width, height):
        """Gambar siluet bale-bale bambu di sudut ruangan."""
        by = int(height * 0.68)
        bx1 = int(width * 0.08)
        bx2 = int(width * 0.92)
        # Permukaan dipan bambu
        draw.rectangle([bx1, by, bx2, by + 28], fill=(6, 5, 4))
        # Kaki dipan bambu
        for leg_x in [bx1 + 30, bx1 + 180, bx2 - 180, bx2 - 30]:
            draw.rectangle([leg_x, by + 28, leg_x + 22, int(height * 0.88)], fill=(5, 4, 3))

    def draw_lampu_ublik(self, draw, lx, ly, flame_h, flicker_val):
        """Gambar lampu minyak tanah (ublik/templok) tradisional dan lidah api hidup."""
        # Botol kaleng/kaca wadah minyak
        draw.ellipse([lx - 28, ly - 10, lx + 28, ly + 40], fill=(12, 10, 8))
        draw.rectangle([lx - 16, ly - 35, lx + 16, ly - 10], fill=(22, 18, 14))
        draw.ellipse([lx - 12, ly - 42, lx + 12, ly - 35], fill=(35, 28, 20))
        
        # Lidah api warm amber (bergetar ditiup angin malam)
        flame_tilt = math.sin(flicker_val * 4.0) * 8.0
        p_top = (lx + flame_tilt, ly - 42 - flame_h)
        p_left = (lx - 14, ly - 42)
        p_right = (lx + 14, ly - 42)
        draw.polygon([p_left, p_top, p_right], fill=(255, 185, 45))
        
        # Inti api putih-kuning
        p_core_top = (lx + flame_tilt * 0.6, ly - 42 - flame_h * 0.55)
        p_core_left = (lx - 7, ly - 42)
        p_core_right = (lx + 7, ly - 42)
        draw.polygon([p_core_left, p_core_top, p_core_right], fill=(255, 245, 180))

    def draw_human_silhouette(self, draw, cx, cy, caping=True, scale=1.0, breathing=0.0):
        """Gambar siluet pria desa duduk waspada memegang caping bambu."""
        cy_adj = cy + breathing * 8.0
        
        # Tubuh / Punggung siluet hitam pekat
        body_points = [
            (cx - 85 * scale, cy_adj + 240 * scale),
            (cx - 70 * scale, cy_adj + 60 * scale),
            (cx - 35 * scale, cy_adj - 20 * scale),
            (cx + 35 * scale, cy_adj - 20 * scale),
            (cx + 70 * scale, cy_adj + 60 * scale),
            (cx + 85 * scale, cy_adj + 240 * scale),
        ]
        draw.polygon(body_points, fill=(2, 2, 2))
        
        # Kepala
        head_radius = 42 * scale
        draw.ellipse([cx - head_radius, cy_adj - 70 * scale - head_radius, 
                      cx + head_radius, cy_adj - 70 * scale + head_radius], fill=(2, 2, 2))
        
        # Caping bambu (topi kerucut)
        if caping:
            cap_w = 175 * scale
            cap_h = 75 * scale
            cap_top = (cx, cy_adj - 130 * scale)
            cap_left = (cx - cap_w, cy_adj - 65 * scale)
            cap_right = (cx + cap_w, cy_adj - 65 * scale)
            draw.polygon([cap_left, cap_top, cap_right], fill=(3, 3, 2))

    def draw_entity_silhouette(self, draw, cx, cy, scale=1.0, sway=0.0, eye_alpha=0.0):
        """Gambar siluet entitas folklor jangkung dengan jari kuku memanjang."""
        cx_adj = cx + sway * 15.0
        
        # Badan jangkung melengkung
        body = [
            (cx_adj - 50 * scale, cy + 380 * scale),
            (cx_adj - 35 * scale, cy - 80 * scale),
            (cx_adj, cy - 220 * scale),
            (cx_adj + 45 * scale, cy - 80 * scale),
            (cx_adj + 60 * scale, cy + 380 * scale),
        ]
        draw.polygon(body, fill=(1, 1, 1))
        
        # Kepala ganjil tanpa leher
        draw.ellipse([cx_adj - 35 * scale, cy - 280 * scale, 
                      cx_adj + 35 * scale, cy - 210 * scale], fill=(1, 1, 1))
        
        # Lengan panjang menjuntai dengan jari kuku
        left_arm = [(cx_adj - 40 * scale, cy - 60 * scale), 
                    (cx_adj - 95 * scale, cy + 120 * scale), 
                    (cx_adj - 110 * scale, cy + 280 * scale)]
        draw.line(left_arm, fill=(1, 1, 1), width=int(18 * scale))
        
        # Jari-jari mencakar
        for f_angle in [-0.3, 0.0, 0.3]:
            fx = cx_adj - 110 * scale + math.sin(f_angle) * 35 * scale
            fy = cy + 280 * scale + math.cos(f_angle) * 45 * scale
            draw.line([(cx_adj - 110 * scale, cy + 280 * scale), (fx, fy)], fill=(1, 1, 1), width=int(5 * scale))
            
        # Mata berpendar samar (jika ada pemicu horor)
        if eye_alpha > 0.05:
            e_col = (int(255 * eye_alpha), int(240 * eye_alpha), int(200 * eye_alpha))
            draw.ellipse([cx_adj - 14 * scale, cy - 250 * scale, cx_adj - 6 * scale, cy - 242 * scale], fill=e_col)
            draw.ellipse([cx_adj + 6 * scale, cy - 250 * scale, cx_adj + 14 * scale, cy - 242 * scale], fill=e_col)

    def draw_shadow_projection(self, draw, sx, sy, scale=1.0, stretch=1.0):
        """Gambar bayangan raksasa terproyeksi di dinding gedhek bambu."""
        shadow_poly = [
            (sx - 120 * scale, sy + 300 * scale),
            (sx - 90 * scale * stretch, sy - 150 * scale * stretch),
            (sx, sy - 380 * scale * stretch),
            (sx + 110 * scale * stretch, sy - 150 * scale * stretch),
            (sx + 140 * scale, sy + 300 * scale),
        ]
        draw.polygon(shadow_poly, fill=(4, 3, 3, 140))

    def render_subtitle(self, draw, text, width, height):
        """Render teks subtitle bergaya temaram di area aman (safe-zone)."""
        if not text:
            return
            
        y_pos = int(height * 0.65) # Area aman 35% dari dasar layar (9:16)
        
        # Ukur teks
        bbox = self.font_sub.getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x_pos = (width - tw) // 2
        
        # Pendaran luar (outer glow) amber hangat
        for ox in [-3, -2, -1, 0, 1, 2, 3]:
            for oy in [-3, -2, -1, 0, 1, 2, 3]:
                if ox != 0 or oy != 0:
                    draw.text((x_pos + ox, y_pos + oy), text, font=self.font_sub, fill=(180, 100, 20, 90))
                    
        # Bayangan hitam pekat
        for ox in [-1, 1]:
            for oy in [-1, 1]:
                draw.text((x_pos + ox, y_pos + oy), text, font=self.font_sub, fill=(0, 0, 0, 220))
                
        # Teks utama warna putih gading hangat
        draw.text((x_pos, y_pos), text, font=self.font_sub, fill=(255, 248, 230))

    def render_frame(self, frame_num, total_frames, scene_config):
        """Render 1 frame tunggal beresolusi penuh."""
        w, h = self.width, self.height
        t = frame_num / self.fps
        
        # Dinamika kedipan api (flicker)
        flicker = math.sin(t * 14.0) * 0.5 + math.sin(t * 23.0) * 0.3 + math.sin(t * 7.0) * 0.2
        light_radius = (h * 0.52) * (1.0 + 0.08 * flicker)
        
        lx = int(w * 0.50 + math.sin(t * 1.5) * 6.0)
        ly = int(h * 0.66)
        flame_height = 42 + 10 * flicker
        
        # 1. Gradien dasar pencahayaan warm amber chiaroscuro
        inner_amber = (72, 42, 14)
        outer_dark = (5, 6, 8)
        base_arr = self.create_radial_gradient(lx, ly, light_radius, inner_amber, outer_dark)
        img = Image.fromarray(base_arr, mode="RGB").convert("RGBA")
        overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        # 2. Gambar dinding anyaman gedhek bambu
        self.draw_gedhek_texture(draw, w, h, lx, ly, t)
        
        # 3. Lantai tanah dan dipan bale-bale bambu
        self.draw_floor(draw, w, h)
        self.draw_bale_bambu(draw, w, h)
        
        # 4. Proyeksi bayangan di dinding
        shadow_stretch = 1.0 + 0.15 * math.sin(t * 3.0)
        self.draw_shadow_projection(draw, int(w * 0.68), int(h * 0.42), scale=1.3, stretch=shadow_stretch)
        
        # 5. Siluet entitas horor (jika aktif di adegan ini)
        if scene_config.get("show_entity", False):
            eye_p = scene_config.get("eye_glow", 0.0)
            self.draw_entity_silhouette(draw, int(w * 0.75), int(h * 0.46), scale=1.2, sway=math.sin(t * 2.0), eye_alpha=eye_p)
            
        # 6. Siluet manusia ber-caping di foreground
        breathing = math.sin(t * 2.5) * 0.4
        self.draw_human_silhouette(draw, int(w * 0.35), int(h * 0.58), caping=True, scale=1.1, breathing=breathing)
        
        # 7. Lampu ublik/minyak di atas meja
        self.draw_lampu_ublik(draw, lx, ly, flame_height, t)
        
        # 8. Lapisan kabut merayap
        self.draw_fog_layer(draw, w, h, frame_num, layer_offset=0)
        self.draw_fog_layer(draw, w, h, frame_num, layer_offset=35)
        
        # 9. Subtitle teks
        sub_text = scene_config.get("subtitle", "")
        self.render_subtitle(draw, sub_text, w, h)
        
        # Gabungkan overlay ke gambar dasar
        final_img = Image.alpha_composite(img, overlay).convert("RGB")
        return final_img
