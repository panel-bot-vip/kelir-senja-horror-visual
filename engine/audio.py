"""
Kelir Senja - Horror Soundscape & Audio Synthesizer
Developer: Wanz
Menghasilkan atmosfer suara horor malam Nusantara (drone mistis, desis sumbu api, jangkrik malam, detak jantung).
"""

import numpy as np
import wave
import struct
import math
import subprocess
import os

def generate_horror_soundscape(output_wav_path, duration_seconds=10.0, sample_rate=48000):
    total_samples = int(duration_seconds * sample_rate)
    t = np.linspace(0, duration_seconds, total_samples, endpoint=False)
    
    # 1. Sub-bass horror drone (frekuensi rendah 42 Hz - 48 Hz berdenyut lambat)
    drone_freq = 45.0 + 3.0 * np.sin(2 * np.pi * 0.15 * t)
    drone = 0.28 * np.sin(2 * np.pi * drone_freq * t)
    
    # Harmonisasi nada mistis (Gamelan degung disonansi nada slendro: 184 Hz & 236 Hz sangat pelan)
    gamelan_tone = 0.04 * np.sin(2 * np.pi * 184.0 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.08 * t))
    gamelan_tone += 0.03 * np.sin(2 * np.pi * 236.0 * t)
    
    # 2. Desir angin malam basah (filtered noise)
    noise = np.random.uniform(-1.0, 1.0, total_samples)
    # Moving average filter untuk membuat desir angin lembut
    window = 120
    wind = np.convolve(noise, np.ones(window)/window, mode='same') * 0.35
    wind *= (0.5 + 0.5 * np.sin(2 * np.pi * 0.22 * t))
    
    # 3. Suara jangkrik malam (crickets)
    crickets = np.zeros(total_samples)
    carrier = np.sin(2 * np.pi * 4500.0 * t)
    burst_mod = (np.sin(2 * np.pi * 18.0 * t) > 0.3).astype(float)
    slow_env = 0.5 * (1.0 + np.sin(2 * np.pi * 0.4 * t))
    crickets = 0.06 * carrier * burst_mod * slow_env
    
    # 4. Detak jantung perlahan (heartbeat thud) setiap 1.2 detik
    heartbeat = np.zeros(total_samples)
    hb_period = 1.25
    for i in range(int(duration_seconds / hb_period)):
        start_t = i * hb_period
        idx_start = int(start_t * sample_rate)
        # Thud 1 (Lub)
        dur1 = int(0.12 * sample_rate)
        if idx_start + dur1 < total_samples:
            tt1 = np.linspace(0, 0.12, dur1)
            heartbeat[idx_start:idx_start+dur1] += 0.30 * np.sin(2 * np.pi * 55.0 * tt1) * np.exp(-tt1 * 25.0)
        # Thud 2 (Dub)
        idx_dub = idx_start + int(0.22 * sample_rate)
        dur2 = int(0.14 * sample_rate)
        if idx_dub + dur2 < total_samples:
            tt2 = np.linspace(0, 0.14, dur2)
            heartbeat[idx_dub:idx_dub+dur2] += 0.22 * np.sin(2 * np.pi * 48.0 * tt2) * np.exp(-tt2 * 20.0)
            
    # Gabungkan semua lapisan suara
    master_mix = drone + gamelan_tone + wind + crickets + heartbeat
    
    # Fade in & Fade out 0.5 detik di ujung audio
    fade_samples = int(0.5 * sample_rate)
    fade_in = np.linspace(0.0, 1.0, fade_samples)
    fade_out = np.linspace(1.0, 0.0, fade_samples)
    master_mix[:fade_samples] *= fade_in
    master_mix[-fade_samples:] *= fade_out
    
    # Normalisasi agar tidak clipping
    max_val = np.max(np.abs(master_mix))
    if max_val > 0.001:
        master_mix = (master_mix / max_val) * 0.85
        
    # Konversi ke 16-bit PCM WAV stereo
    stereo_mix = np.vstack((master_mix, master_mix)).T
    pcm_data = (stereo_mix * 32767).astype(np.int16)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_wav_path)), exist_ok=True)
    with wave.open(output_wav_path, 'w') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_data.tobytes())
        
    return output_wav_path

def mix_audio_with_voiceover(vo_path, horror_bed_path, output_path):
    """Campur audio voiceover dengan musik/SFX di 50% (-6dB)."""
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-i", vo_path,
        "-i", horror_bed_path,
        "-filter_complex",
        "[1:a]volume=0.45[bed];[0:a][bed]amix=inputs=2:duration=first:dropout_transition=2[out]",
        "-map", "[out]",
        "-ar", "48000", "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    subprocess.run(cmd, check=True)
    return output_path
