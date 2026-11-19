# KELIR SENJA: HORROR VISUAL & ANIMATION SYSTEM
**Developer:** Wanz  
**Versi:** 1.1.0  
**Bahasa:** Penuh Bahasa Indonesia (*Full Indonesian*)  
**Arsip Paket:** `kelir-senja-horror-visual.zip`  
**Repositori GitHub:** [panel-bot-vip/kelir-senja-horror-visual](https://github.com/panel-bot-vip/kelir-senja-horror-visual)

---

## 1. TENTANG SKILL INI
**Kelir Senja Horror Visual System** adalah paket keahlian (*skill package*) khusus untuk Claude yang dirancang oleh developer **Wanz** untuk memandu produksi konten animasi dan visual horor bertema folklor lokal Nusantara. 

Sistem ini menggabungkan filosofi teater bayangan wayang kulit (*kelir*) dengan sinematografi horor modern beresolusi tinggi, di mana karakter ditampilkan dalam bentuk **siluet hitam pekat**, diterangi oleh **cahaya temaram lilin, lampu minyak (teplok/ublik), dan bara dupa kemenyan yang hangat kekuningan (*warm amber chiaroscuro*)**, di tengah kepekatan malam Nusantara yang mencekam.

Selain memandu prompt AI eksternal, kit ini kini dilengkapi dengan **Engine Render Prosedural Internal** yang dapat merender animasi frame demi frame dan menyusunnya menjadi video MP4 utuh secara langsung melalui CLI!

---

## 2. FITUR UTAMA & ATURAN SISTEM

### 🎬 A. Alur Percakapan Pembuka Otomatis (Mandatory Intake)
Ketika skill ini digunakan pertama kali, Claude akan langsung menanyakan dua hal wajib:
1. **Status Naskah:**
   - **Opsi 1 (Sudah punya Voiceover/Naskah):** Pengguna cukup mengirimkan audio atau teks naskah, lalu Claude langsung membedahnya menjadi breakdown adegan, timecode subtitle, prompt animasi, atau berkas timeline JSON siap render.
   - **Opsi 2 (Belum punya naskah):** Claude langsung menyajikan **10 Ide Cerita Horor Folklor Lokal** yang mencekam, meminta pengguna memilih 1 ide, lalu menyusunkan naskah voiceover lengkapnya.
2. **Pilihan Rasio Visual:**
   - **9:16 (Vertikal):** Untuk TikTok, Instagram Reels, dan YouTube Shorts.
   - **16:9 (Horizontal):** Untuk YouTube Widescreen dan tampilan sinematik lanskap.

### 🛡️ B. Produksi Berbagian & Kartu Checkpoint Anti-Limit
- Produksi adegan tidak pernah ditumpuk dalam satu pesan panjang, melainkan dipecah secara berurutan: **Bagian 1**, **Bagian 2**, **Bagian 3**, hingga **Bagian [N] - Tamat**.
- Setiap bagian menyertakan **Kartu Checkpoint** di akhir pesan. Jika sesi Claude terputus atau batas limit pesan tercapai, pengguna cukup menyalin kartu checkpoint tersebut ke obrolan baru dan mengetik `"Lanjutkan ke Bagian X"` untuk meneruskan tepat dari adegan berikutnya tanpa mengulang.

### 📝 C. Integrasi Subtitle Lengkap
- Setiap adegan dilengkapi teks subtitle, estimasi timecode detik-ke-detik, penataan tipografi (warna pendar gading/amber), serta zona aman (*safe zone*) agar tidak tertutup antarmuka media sosial.
- Di akhir bagian tamat, disediakan kompilasi naskah berformat file `.srt` siap pakai untuk CapCut, Adobe Premiere, atau VN Editor.

### 🎥 D. Render Langsung ke MP4 (CLI Video Generation)
- Menggunakan `engine/render.py` untuk menggambar frame animasi bergaya siluet gelap, efek api lentera berkedip (*flickering flame*), bayangan dinding gedhek, kabut tanah, dan subtitle yang menempel rapi.
- Menggunakan `engine/audio.py` untuk mensintesis audio atmosferik horor (sub-bass drone, desis angin, derik jangkrik, dan detak jantung).
- Menghasilkan file video `.mp4` 1080x1920 (9:16) atau 1920x1080 (16:9) pada 30fps secara otomatis.

---

## 3. STRUKTUR BERKAS DI DALAM PAKET

```text
kelir-senja-horror-visual/
├── SKILL.md                                 # Berkas instruksi master skill untuk Claude
├── README.md                                # Dokumentasi lengkap, instalasi, dan panduan pakai
├── engine/                                  # Mesin animasi dan audio generator
│   ├── render.py                            # Frame generator siluet, cahaya lilin, gedhek, kabut
│   └── audio.py                             # Synthesizer audio drone horor, jangkrik, angin, SFX
├── tools/                                   # Skrip eksekusi CLI
│   ├── render_video.py                      # Skrip utama perender frame ke video MP4
│   ├── burn_subtitles.py                    # Tool pembakar subtitle SRT ke MP4
│   └── setup.sh                             # Skrip instalasi & verifikasi dependensi
├── modules/                                 # Modul pedoman teknis mendalam
│   ├── 01_panduan_karakter_siluet.md        # Anatomi siluet, postur, pendaran mata, entitas gaib
│   ├── 02_pencahayaan_dan_properti_lokal.md # Lampu templok, lilin, anyaman gedhek, kendi, kemenyan
│   ├── 03_sinematografi_dan_kamera.md       # Komposisi 9:16 vs 16:9, low-angle dread, dutch angle
│   ├── 04_dinamika_animasi_dan_gerakan.md   # Pacing creeping dread, kedipan api, hembusan kain
│   ├── 05_alam_dan_vegetasi_mistis.md       # Rumpun bambu, pohon beringin, randu, kabut tanah
│   ├── 06_arsitektur_dan_bangunan_kuno.md   # Dinding gedhek, rumah panggung, joglo lapuk, sumur tua
│   ├── 07_generator_prompt_adegan.md        # Formula prompt Midjourney, Flux, Kling, Runway, Luma
│   └── 08_panduan_subtitle_dan_tipografi.md # Standar subtitle, warna amber glow, timing, format SRT
├── workflows/                               # Alur kerja dan prosedur sistem
│   ├── 01_alur_interaksi_awal.md            # Dialog pohon keputusan intake naskah & resolusi
│   └── 02_sistem_chunking_dan_checkpoint.md # Mekanisme pemecahan bagian dan pemulihan batas kuota
├── templates/                               # Lembar kerja siap pakai
│   ├── template_rekap_adegan.md             # Format standar lembar kerja per adegan
│   ├── template_checkpoint_recovery.md      # Format kartu pemulihan sesi antar-chat
│   └── template_prompt_ai_generator.md      # Bank kata kunci dan formula prompt baku
├── examples/                                # Contoh penerapan nyata
│   ├── 10_ide_cerita_folklor_lokal.md       # Bank 10 ide cerita horor folklor Nusantara siap pakai
│   └── contoh_produksi_lengkap_bagian_1_sampai_tamat.md # Contoh simulasi utuh Bagian 1 s/d Tamat
└── example/
    └── cerita_ublik.json                    # Timeline adegan siap render langsung
```

---

## 4. CARA MENJALANKAN RENDER VIDEO MP4

Jalankan perintah berikut di terminal:

```bash
# 1. Jalankan verifikasi dependensi
bash tools/setup.sh

# 2. Render video MP4 dari cerita JSON
python3 tools/render_video.py --story example/cerita_ublik.json --out out/misteri_lampu_ublik.mp4

# 3. (Opsional) Tempelkan file subtitle SRT ke video
python3 tools/burn_subtitles.py --input out/misteri_lampu_ublik.mp4 --srt example/subtitles.srt --output out/misteri_lampu_ublik_subbed.mp4
```

---

## 5. PANDUAN PENGGUNAAN DI CLAUDE

### Metode 1: Penggunaan di Claude Projects (Sangat Direkomendasikan)
1. Ekstrak file `kelir-senja-horror-visual.zip`.
2. Buka akun **Claude.ai** dan buat Project baru (misal: *Produksi Horor Kelir Senja*).
3. Salin isi berkas `SKILL.md` ke dalam kolom **Custom Instructions (Instruksi Khusus Proyek)**.
4. Unggah seluruh file di folder `modules/`, `workflows/`, `templates/`, dan `examples/` ke dalam bagian **Project Knowledge**.
5. Mulai obrolan baru di dalam Project tersebut. Claude akan langsung menyapa dengan pertanyaan alur intake awal!

### Metode 2: Penggunaan di Obrolan Biasa (Claude Free / Pro Chat)
1. Buka berkas `SKILL.md`.
2. Salin seluruh teksnya dan kirimkan sebagai pesan pertama di obrolan baru Claude.
3. Claude akan otomatis mengunci persona *Kelir Senja* dan memulai sesi kerja dengan menanyakan kesiapan naskah dan rasio.

---

## 6. KREDIT & LISENSI
- **Pencipta / Developer:** Wanz
- **Hak Cipta:** 2026 Wanz - Kelir Senja Visual Productions.
- Bebas digunakan untuk keperluan produksi konten kreatif komersial maupun non-komersial.
