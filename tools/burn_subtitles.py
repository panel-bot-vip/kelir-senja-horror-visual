#!/usr/bin/env python3
"""
Kelir Senja - Tool Pembakar Subtitle (.SRT ke MP4)
Developer: Wanz
Penggunaan:
  python3 tools/burn_subtitles.py --input video.mp4 --srt subtitles.srt --output video_subbed.mp4
"""

import argparse
import subprocess
import os
import sys

def burn_srt(input_mp4, srt_file, output_mp4):
    if not os.path.exists(input_mp4):
        raise FileNotFoundError(f"File video tidak ditemukan: {input_mp4}")
    if not os.path.exists(srt_file):
        raise FileNotFoundError(f"File subtitle SRT tidak ditemukan: {srt_file}")
        
    print(f"🎬 Menempelkan subtitle '{srt_file}' ke dalam video...")
    
    # Filter subtitles FFmpeg dengan styling Kelir Senja (Font Serif, Warm Cream, Black Outline)
    style = "FontName=DejaVu Serif,FontSize=22,PrimaryColour=&H00E0F6FF,OutlineColour=&H00000000,BackColour=&H60000000,Bold=1,Outline=2,Shadow=1,Alignment=2,MarginV=120"
    sub_filter = f"subtitles='{srt_file}':force_style='{style}'"
    
    cmd = [
        "ffmpeg", "-y", "-v", "warning",
        "-i", input_mp4,
        "-vf", sub_filter,
        "-c:v", "libx264", "-crf", "18", "-preset", "fast",
        "-c:a", "copy",
        output_mp4
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Selesai! Video dengan subtitle tersimpan di: {output_mp4}")

def main():
    parser = argparse.ArgumentParser(description="Kelir Senja Subtitle Burner by Wanz")
    parser.add_argument("--input", required=True, help="Video MP4 masukan")
    parser.add_argument("--srt", required=True, help="File subtitle .srt")
    parser.add_argument("--output", required=True, help="Path video MP4 keluaran")
    args = parser.parse_args()
    burn_srt(args.input, args.srt, args.output)

if __name__ == "__main__":
    main()
