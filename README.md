# KELIR SENJA: HORROR VISUAL & ANIMATION SYSTEM
**Developer:** Wanz  
**Versi:** 1.2.1  
**Bahasa:** Penuh Bahasa Indonesia (*Full Indonesian*)  
**Arsip Paket:** `kelir-senja-horror-visual.zip`  
**Repositori GitHub:** [panel-bot-vip/kelir-senja-horror-visual](https://github.com/panel-bot-vip/kelir-senja-horror-visual)

---

## 1. TENTANG SKILL INI
**Kelir Senja Horror Visual System** adalah paket keahlian (*skill package*) khusus untuk Claude yang dirancang oleh developer **Wanz** untuk memandu produksi konten animasi dan visual horor bertema folklor lokal Nusantara. 

Sistem ini menggabungkan filosofi teater bayangan wayang kulit (*kelir*) dengan sinematografi horor modern beresolusi tinggi, di mana karakter ditampilkan dalam bentuk **siluet hitam pekat**, diterangi oleh **cahaya temaram lilin, lampu minyak (teplok/ublik), dan bara dupa kemenyan yang hangat kekuningan (*warm amber chiaroscuro*)**, di tengah kepekatan malam Nusantara yang mencekam.

Selain memandu prompt AI, kit ini dilengkapi dengan **Engine Render Prosedural Internal** yang dapat merender animasi frame demi frame dan menyusunnya menjadi video MP4 utuh secara langsung melalui CLI dengan voiceover pengguna!

---

## 2. 🎙️ PROMPT MASTER PEMBUAT NASKAH VOICEOVER (SIAP SALIN)

> **💡 Klik tombol salin (copy) pada pojok kanan atas kotak kode di bawah ini. Hasil dari prompt ini HANYA teks narasi voiceover murni tanpa nomor, tanpa scene, dan tanpa subtitle—sehingga langsung siap Anda rekam ke mikrofon!**

```markdown
Kamu adalah seorang Penulis Naskah Voiceover Horor Folklor Nusantara bergaya "Kelir Senja".

Tugasmu: Tulis naskah voiceover cerita horor lokal yang sangat dingin, mencekam, bertempo lambat, dan diakhiri pelintiran cerita (twist) yang mengejutkan di kalimat penutup.

### ATURAN UTAMA OUTPUT (WAJIB DIPATUHI):
1. HANYA berikan teks voiceover murni yang siap langsung dibaca/direkam ke mikrofon.
2. DILARANG menyertakan nomor, adegan, bagian (Scene 1, Scene 2, dll).
3. DILARANG menyertakan teks subtitle, timecode, petunjuk teknis, atau catatan pengantar/penutup.
4. Gunakan bahasa Indonesia naratif dengan diksi folklor lokal (seperti lampu ublik, gedhek, bale bambu, kain mori, sangkala).
5. Struktur narasi: Hook pembuka larangan adat -> suasana malam bilik bambu -> eskalasi gangguan gaib -> twist penutup yang dingin.
6. Panjang naskah: sekitar 60 - 80 kata (durasi baca hening sekitar 20 - 30 detik).

---
Pilih 1 dari 10 ide cerita horor folklor Nusantara berikut (atau gunakan topik yang diberikan user):
1. Pantangan meniup lampu ublik sebelum fajar.
2. Ketukan tiga kali di celah anyaman gedhek.
3. Beban berat di tali timba sumur tua.
4. Mangkuk sesaji di bawah pohon beringin.
5. Derit bale bambu kosong di tengah malam.
6. Selendang merah di rumpun bambu petung.
7. Iring-iringan keranda tanpa jejak kaki.
8. Bau kemenyan di lumbung padi kuno.
9. Suara tangis dari kolong rumah panggung.
10. Jenazah yang matanya menolak terpejam.

Sekarang, langsung tuliskan TEKS VOICEOVER-NYA SAJA:
```

---

## 3. FITUR UTAMA & ATURAN SISTEM

### 🎬 A. Alur Percakapan Pembuka Otomatis (Mandatory Intake)
Ketika skill ini digunakan pertama kali, Claude akan langsung menanyakan dua hal wajib:
1. **Status Naskah / Voiceover:**
   - **Opsi 1 (Sudah punya Voiceover):** Pengguna mengirimkan file audio voiceover (`.mp3`/`.wav`/dll). Claude langsung memproses durasi, menggambar frame animasi, mencampurkan audio, membakar subtitle, dan mengirimkan file video MP4 jadinya!
   - **Opsi 2 (Belum punya naskah):** Claude langsung menyajikan **10 Ide Cerita Horor Folklor Lokal** yang mencekam, meminta pengguna memilih 1 ide, lalu menyusunkan teks voiceover murni untuk direkam/dikirimkan.
2. **Pilihan Rasio Visual:**
   - **9:16 (Vertikal):** Untuk TikTok, Instagram Reels, dan YouTube Shorts.
   - **16:9 (Horizontal):** Untuk YouTube Widescreen dan tampilan sinematik lanskap.

### 🛡️ B. Produksi Berbagian & Kartu Checkpoint Anti-Limit
- Produksi adegan tidak pernah ditumpuk dalam satu pesan panjang, melainkan dipecah secara berurutan: **Bagian 1**, **Bagian 2**, **Bagian 3**, hingga **Bagian [N] - Tamat**.
- Setiap bagian menyertakan **Kartu Checkpoint** di akhir pesan. Jika sesi Claude terputus atau batas limit pesan tercapai, pengguna cukup menyalin kartu checkpoint tersebut ke obrolan baru dan mengetik `"Lanjutkan ke Bagian X"` untuk meneruskan tepat dari adegan berikutnya tanpa mengulang.

### 📝 C. Integrasi Subtitle Lengkap
- Di dalam video hasil render MP4, subtitle secara otomatis dibakar di area aman (*safe zone*) agar tidak tertutup antarmuka media sosial.
- Di akhir bagian tamat, disediakan kompilasi naskah berformat file `.srt` siap pakai jika dibutuhkan untuk editing lanjutan.

### 🎥 D. Render Langsung ke MP4 (CLI Video Generation)
- Menggunakan `engine/render.py` untuk menggambar frame animasi bergaya siluet gelap, efek api lentera berkedip (*flickering flame*), bayangan dinding gedhek, kabut tanah, dan subtitle yang menempel rapi.
- Menggunakan `engine/audio.py` untuk mensintesis audio atmosferik horor (sub-bass drone, desis angin, derik jangkrik, dan detak jantung) dan memadukannya dengan voiceover kiriman pengguna.
- Menghasilkan file video `.mp4` 1080x1920 (9:16) atau 1920x1080 (16:9) pada 30fps secara otomatis.

---

## 4. STRUKTUR BERKAS DI DALAM PAKET

```text
kelir-senja-horror-visual/
├── SKILL.md                                 # Berkas instruksi master skill untuk Claude
├── README.md                                # Dokumentasi lengkap, instalasi, dan panduan pakai
├── engine/                                  # Mesin animasi dan audio generator
│   ├── render.py                            # Frame generator siluet, cahaya lilin, gedhek, kabut
│   └── audio.py                             # Synthesizer audio drone horor, jangkrik, angin & mixer VO
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
│   ├── prompt_pembuat_naskah_voiceover.md   # Master prompt generator naskah VO murni
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

## 5. CARA MENJALANKAN RENDER VIDEO MP4 DENGAN VOICEOVER

Jalankan perintah berikut di terminal:

```bash
# 1. Jalankan verifikasi dependensi
bash tools/setup.sh

# 2. Render video MP4 menggunakan Voiceover kiriman pengguna
python3 tools/render_video.py --story example/cerita_ublik.json --vo path/ke/voiceover.mp3 --out out/video_horor.mp4

# 3. (Opsional) Tempelkan file subtitle SRT ke video
python3 tools/burn_subtitles.py --input out/video_horor.mp4 --srt example/subtitles.srt --output out/video_subbed.mp4
```

---

## 6. PANDUAN PENGGUNAAN DI CLAUDE

### Metode 1: Penggunaan di Claude Projects (Sangat Direkomendasikan)
1. Ekstrak file `kelir-senja-horror-visual.zip`.
2. Buka akun **Claude.ai** dan buat Project baru (misal: *Produksi Horor Kelir Senja*).
3. Salin isi berkas `SKILL.md` ke dalam kolom **Custom Instructions (Instruksi Khusus Proyek)**.
4. Unggah seluruh file di folder `modules/`, `workflows/`, `templates/`, dan `examples/` ke dalam bagian **Project Knowledge**.
5. Mulai obrolan baru di dalam Project tersebut. Claude akan langsung menyapa dengan pertanyaan alur intake awal!

### Metode 2: Penggunaan di Obrolan Biasa (Claude Free / Pro Chat)
1. Buka berkas `SKILL.md`.
2. Salin seluruh teksnya dan kirimkan sebagai pesan pertama di obrolan baru Claude.
3. Claude akan otomatis mengunci persona *Kelir Senja* dan memulai sesi kerja dengan menanyakan kesiapan voiceover dan rasio.

---

## 7. KREDIT & LISENSI
- **Pencipta / Developer:** Wanz
- **Hak Cipta:** 2026 Wanz - Kelir Senja Visual Productions.
- Bebas digunakan untuk keperluan produksi konten kreatif komersial maupun non-komersial.
