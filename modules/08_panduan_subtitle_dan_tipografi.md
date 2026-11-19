# MODUL 08: PANDUAN SUBTITLE, TIPOGRAFI & SINKRONISASI AUDIO-VISUAL
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

---

## 1. PRINSIP DASAR SUBTITLE GAYA "KELIR SENJA"
Subtitle dalam konten horor bukan sekadar teks terjemahan atau penjelas kata-kata, melainkan elemen visual yang ikut membangun atmosfer mencekam. Penataan teks subtitle harus selaras dengan estetika siluet hitam dan pencahayaan hangat temaram (*warm amber*).

### Karakteristik Estetika Teks Subtitle:
1. **Tipografi Bersahaja & Mistis:**
   - Rekomendasi Font: Serif klasik dengan nuansa tua dan elegan (misalnya: *Cinzel*, *Cormorant Garamond*, *Playfair Display*, *EB Garamond*) atau font sans-serif bersih bertipe tebal untuk keterbacaan tinggi di ponsel (*Montserrat Bold*, *The Bold Font*, *Bebas Neue*).
   - Hindari font komik, font futuristik sci-fi, atau font tulisan tangan kuas yang berlebihan hingga sulit dibaca.
2. **Palet Warna & Efek Cahaya (Glow & Contrast):**
   - **Warna Teks Utama:** Putih kapur kusam (*chalk white #F0EFEA*) atau kuning krem temaram (*warm bone cream #FFF3D6*).
   - **Efek Pendaran Halus (Subtle Amber Glow):** Berikan efek pendar tipis (*outer glow*) berwarna jingga keemasan (*warm amber #FF9F1C* atau #E28743) dengan intensitas lembut (radius pendar 2-4px), meniru efek cahaya lampu minyak di sekeliling huruf.
   - **Garis Tepi / Bayangan (Drop Shadow / Stroke):** Outline hitam pekat lembut (*soft black drop shadow*) 1-2px agar teks selalu terbaca kontras di atas latar belakang malam, kabut, maupun percikan api.
3. **Zona Aman Penempatan Teks (Safe Area Guidelines):**
   - **Format Vertikal (9:16 - TikTok / IG Reels / YouTube Shorts):**
     - Letakkan teks di area tengah bawah (antara 30% hingga 40% dari batas bawah layar).
     - **PENTING:** Jangan letakkan teks tepat di bagian bawah layar (0-20% bawah) karena akan tertutup oleh judul video, tombol deskripsi, dan ikon aplikasi media sosial.
     - Hindari menutupi bagian fokus siluet utama (seperti tangan yang memegang lilin atau wajah sosok misterius).
   - **Format Horizontal (16:9 - YouTube / Sinematik):**
     - Letakkan teks di area sepertiga bawah tengah (*lower third center*), dengan margin bawah sekitar 10-12% dari garis tepi dasar.

---

## 2. RITME PEMENGGALAN & TIMING SUBTITLE (PACING)
1. **Aturan Panjang Kata (Word Chunking):**
   - Maksimal 3 hingga 6 kata per tampilan layar (jangan biarkan kalimat panjang bertumpuk 3 baris).
   - Tampilkan teks secara bertahap mengikuti ritme jeda napas voiceover (*spoken sentence pauses*).
2. **Animasi Kemunculan Teks:**
   - **Gaya Fade-in Lembut:** Teks muncul dengan transisi transparansi halus (0.1 - 0.2 detik), seolah perlahan terlihat dari balik kabut.
   - **Gaya Word-by-Word Reveal (Opsional untuk Shorts/Reels):** Kata aktif yang sedang diucapkan berpendar warna kuning lilin hangat, sementara kata sebelumnya berwarna putih redup.
   - Hindari animasi teks yang melompat-lompat berlebihan (*bouncy pop-up*) yang merusak suasana hening dan menakutkan.

---

## 3. FORMAT OUTPUT SUBTITLE DALAM PRODUKSI ADEGAN
Setiap adegan yang dirancang di dalam Bagian 1 sampai Tamat wajib menyertakan blok arahan subtitle lengkap:

```markdown
- **Teks Subtitle:** "[Potongan naskah yang tampil di layar]"
- **Estimasi Timecode:** [00:00 - 00:03] (Durasi: 3 detik)
- **Pemenggalan Baris:**
  Baris 1: [Kata-kata 1]
  Baris 2: [Kata-kata 2]
- **Pengaturan Visual Subtitle:**
  - Warna: Kuning gading hangat (#FFF5DD) dengan bayangan hitam pekat
  - Posisi: Tengah bawah (vertikal 35% dari dasar layar untuk 9:16)
  - Animasi: Fade in 0.15 detik, diam saat dibacakan, fade out lembut
```

---

## 4. CONTOH FORMAT SIAP PAKAI SRT (SUBRIP SUBTITLE)
Jika user membutuhkan file atau teks berformat `.srt` untuk langsung diimpor ke aplikasi editing (CapCut, Premiere Pro, DaVinci Resolve, VN):

```srt
1
00:00:00,000 --> 00:00:03,200
Malam itu, di bilik bambu reot pinggir desa...

2
00:00:03,200 --> 00:00:06,500
nyala lampu templok mendadak padam ditiup napas dingin.

3
00:00:06,500 --> 00:00:10,000
Dan dari balik celah gedhek, sepasang mata menatap tanpa berkedip.
```

---

## 5. PANDUAN PENGATURAN SUBTITLE DI APLIKASI EDITING POPULER

### A. CapCut (Ponsel & PC)
1. Masuk ke menu **Teks** -> **Keterangan Otomatis (Auto Captions)** atau **Tambahkan Teks**.
2. Pilih font: *Cinzel* atau *Montserrat*.
3. Buka tab **Gaya**:
   - Warna teks: Putih gading / Kuning pucat.
   - Buka opsi **Glow / Bersinar**: Pilih warna oranye hangat atau kuning mustard, atur intensitas 25%, rentang 15%.
   - Buka opsi **Bayangan**: Hitam pekat, buram 20%, jarak 5%.
4. Penataan: Geser kotak teks ke area aman sedikit di atas ikon nama akun TikTok/Reels.

### B. Adobe Premiere Pro
1. Gunakan panel **Text** -> **Create Captions from Transcript**.
2. Pada tab **Essential Graphics**, atur gaya teks:
   - Font: *Cormorant Garamond Bold* atau *Cinzel Decorative*.
   - Fill: `#FFF8E7`
   - Shadow: `#000000`, Opacity 85%, Angle 135°, Distance 4, Blur 8.
