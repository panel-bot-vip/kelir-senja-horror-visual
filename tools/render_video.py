#!/usr/bin/env python3
"""
Kelir Senja - Tool Render Video MP4 Langsung
Developer: Wanz
Fungsi:
  Mengambil file audio voiceover kiriman pengguna (MP3, WAV, M4A, OGG),
  menghitung durasi persisnya, merender frame animasi siluet horor kelir senja,
  membakar subtitle, mencampurkan audio VO asli + soundscape, dan menghasilkan file MP4 final.

Penggunaan:
  python3 tools/render_video.py --story example/cerita_ublik.json --vo path/ke/voiceover_user.mp3 --out out/video_final.mp4
"""

import argparse
import json
import os
import sys
import subprocess
from pathlib import Path

# Tambahkan direktori root skill ke sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from engine.render import KelirSenjaRenderer
from engine.audio import generate_horror_soundscape, mix_audio_with_voiceover, get_audio_duration

def render_story_to_mp4(story_file, output_mp4, width=1080, height=1920, fps=30, vo_file=None):
    with open(story_file, 'r', encoding='utf-8') as f:
        story = json.load(f)
        
    scenes = story.get("scenes", [])
    if not scenes:
        raise ValueError("Cerita tidak memiliki daftar scene!")
        
    temp_dir = BASE_DIR / "work"
    temp_dir.mkdir(exist_ok=True)
    
    # 1. Validasi Voiceover Kiriman Pengguna
    if vo_file and os.path.exists(vo_file):
        vo_dur = get_audio_duration(vo_file)
        print(f"🎙️ File Voiceover Kiriman Pengguna Diterima: {vo_file}")
        print(f"⏱️ Durasi Voiceover Terukur: {vo_dur:.2f} detik")
        total_duration = vo_dur
        # Sinkronkan durasi tiap scene secara proporsional dengan panjang voiceover
        preset_total = sum(s.get("duration", 3.5) for s in scenes)
        scale_factor = vo_dur / preset_total
        for s in scenes:
            s["duration"] = s.get("duration", 3.5) * scale_factor
    else:
        print("⚠️ Catatan: Tidak ada file voiceover yang dilampirkan. Menggunakan durasi default naskah.")
        total_duration = sum(s.get("duration", 3.5) for s in scenes)
        
    total_frames = int(total_duration * fps)
    
    print(f"\n🎬 [Kelir Senja Animation Engine] Memulai Produksi Video MP4:")
    print(f"   - Judul Cerita: {story.get('title', 'Horor Folklor')}")
    print(f"   - Developer: Wanz")
    print(f"   - Format Resolusi: {width}x{height} (FPS: {fps})")
    print(f"   - Total Scene: {len(scenes)} scene ({total_duration:.2f} detik, {total_frames} frame)")
    
    # 2. Olah Audio: Soundscape Horor + Voiceover Kiriman Pengguna
    soundscape_wav = str(temp_dir / "horror_bed.wav")
    print("🔊 Mensintesis audio soundscape horor (sub-bass drone, angin malam, jangkrik, detak jantung)...")
    generate_horror_soundscape(soundscape_wav, duration_seconds=total_duration + 0.5)
    
    if vo_file and os.path.exists(vo_file):
        print("🎚️ Mencampurkan Voiceover Pengguna dengan Soundscape (VO 100%, Horor Bed -8dB)...")
        final_audio_path = str(temp_dir / "final_mixed_audio.wav")
        mix_audio_with_voiceover(vo_file, soundscape_wav, final_audio_path)
    else:
        final_audio_path = soundscape_wav
        
    # 3. Render Frame demi Frame langsung dipipe ke FFmpeg
    os.makedirs(os.path.dirname(os.path.abspath(output_mp4)), exist_ok=True)
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-v", "warning",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{width}x{height}",
        "-r", str(fps),
        "-i", "-",  # pipe frame dari Python
        "-i", final_audio_path,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        output_mp4
    ]
    
    renderer = KelirSenjaRenderer(width=width, height=height, fps=fps)
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    
    current_frame = 0
    print("🎨 Merender frame demi frame animasi siluet ke MP4...")
    
    try:
        for s_idx, scene in enumerate(scenes):
            s_dur = scene.get("duration", 3.5)
            s_frames = int(s_dur * fps)
            sub_text = scene.get("subtitle", "")
            print(f"   -> [Scene {s_idx + 1}/{len(scenes)}] {sub_text[:40]}... ({s_dur:.1f}s)")
            
            for _ in range(s_frames):
                img = renderer.render_frame(current_frame, total_frames, scene)
                raw_bytes = img.tobytes()
                proc.stdin.write(raw_bytes)
                current_frame += 1
                
        proc.stdin.close()
        proc.wait()
    except Exception as e:
        proc.kill()
        raise e
        
    print(f"\n✅ Video MP4 Berhasil Dirender!")
    print(f"📁 Lokasi File: {output_mp4}")
    return output_mp4

def main():
    parser = argparse.ArgumentParser(description="Kelir Senja MP4 Renderer by Wanz")
    parser.add_argument("--story", required=True, help="Path ke file konfigurasi cerita JSON")
    parser.add_argument("--vo", default=None, help="File audio voiceover kiriman pengguna (MP3/WAV/M4A)")
    parser.add_argument("--out", default="out/kelir_senja_video.mp4", help="Path file keluaran MP4")
    parser.add_argument("--width", type=int, default=1080, help="Lebar video (default 1080)")
    parser.add_argument("--height", type=int, default=1920, help="Tinggi video (default 1920)")
    parser.add_argument("--fps", type=int, default=30, help="FPS video (default 30)")
    
    args = parser.parse_args()
    render_story_to_mp4(args.story, args.out, width=args.width, height=args.height, fps=args.fps, vo_file=args.vo)

if __name__ == "__main__":
    main()
