#!/usr/bin/env python3
"""
Kelir Senja - Tool Render Video MP4 Langsung
Developer: Wanz
Penggunaan:
  python3 tools/render_video.py --story example/cerita_ublik.json --out out/video_horor.mp4
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
from engine.audio import generate_horror_soundscape, mix_audio_with_voiceover

def render_story_to_mp4(story_file, output_mp4, width=1080, height=1920, fps=30, vo_file=None):
    with open(story_file, 'r', encoding='utf-8') as f:
        story = json.load(f)
        
    scenes = story.get("scenes", [])
    if not scenes:
        raise ValueError("Cerita tidak memiliki scene!")
        
    total_duration = sum(s.get("duration", 3.0) for s in scenes)
    total_frames = int(total_duration * fps)
    
    print(f"🎬 [Kelir Senja] Memulai Render MP4:")
    print(f"   - Judul Cerita: {story.get('title', 'Horor Folklor')}")
    print(f"   - Resolusi: {width}x{height} (FPS: {fps})")
    print(f"   - Total Scene: {len(scenes)} scene ({total_duration:.1f} detik, {total_frames} frame)")
    
    # 1. Buat Audio Soundscape Horor
    temp_dir = BASE_DIR / "work"
    temp_dir.mkdir(exist_ok=True)
    soundscape_wav = str(temp_dir / "horror_bed.wav")
    final_audio_path = soundscape_wav
    
    print("🔊 Menghasilkan audio soundscape mistis...")
    generate_horror_soundscape(soundscape_wav, duration_seconds=total_duration + 1.0)
    
    # Jika ada voiceover terpisah, campurkan
    if vo_file and os.path.exists(vo_file):
        print(f"🎙️ Mencampurkan Voiceover: {vo_file}")
        mixed_audio = str(temp_dir / "mixed_audio.wav")
        mix_audio_with_voiceover(vo_file, soundscape_wav, mixed_audio)
        final_audio_path = mixed_audio
        
    # 2. Siapkan FFmpeg Pipe
    os.makedirs(os.path.dirname(os.path.abspath(output_mp4)), exist_ok=True)
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-v", "warning",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{width}x{height}",
        "-r", str(fps),
        "-i", "-",  # input dari stdin pipe
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
    print("🎨 Merender frame demi frame ke MP4...")
    
    try:
        for s_idx, scene in enumerate(scenes):
            s_dur = scene.get("duration", 3.0)
            s_frames = int(s_dur * fps)
            sub_text = scene.get("subtitle", "")
            print(f"   -> Merender Scene {s_idx + 1}/{len(scenes)}: \"{sub_text[:35]}...\" ({s_dur}s)")
            
            for f_in_scene in range(s_frames):
                img = renderer.render_frame(current_frame, total_frames, scene)
                raw_bytes = img.tobytes()
                proc.stdin.write(raw_bytes)
                current_frame += 1
                
        proc.stdin.close()
        proc.wait()
    except Exception as e:
        proc.kill()
        raise e
        
    print(f"✅ Video MP4 Berhasil Dibuat!")
    print(f"📁 Lokasi File: {output_mp4}")
    return output_mp4

def main():
    parser = argparse.ArgumentParser(description="Kelir Senja MP4 Renderer by Wanz")
    parser.add_argument("--story", required=True, help="Path ke file konfigurasi cerita JSON")
    parser.add_argument("--out", default="out/kelir_senja_short.mp4", help="Path output video MP4")
    parser.add_argument("--width", type=int, default=1080, help="Lebar video (default 1080)")
    parser.add_argument("--height", type=int, default=1920, help="Tinggi video (default 1920)")
    parser.add_argument("--fps", type=int, default=30, help="FPS video (default 30)")
    parser.add_argument("--vo", default=None, help="File audio voiceover (opsional)")
    
    args = parser.parse_args()
    render_story_to_mp4(args.story, args.out, width=args.width, height=args.height, fps=args.fps, vo_file=args.vo)

if __name__ == "__main__":
    main()
