# WORKFLOW 02: SISTEM CHUNKING & CHECKPOINT ANTI-LIMIT
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

---

## 1. MENGAPA SISTEM CHUNKING DIPERLUKAN?
Model bahasa AI seperti Claude memiliki batas panjang output dalam satu kali pengiriman pesan (*maximum generation token limit*), serta batas jendela konteks percakapan (*context window*). 

Dalam produksi video animasi horor berkualitas tinggi:
1. Setiap adegan memerlukan deskripsi yang sangat mendalam: komposisi kamera, siluet karakter, fisika pencahayaan lampu templok, prompt gambar, motion prompt video, arahan SFX, serta timing teks subtitle.
2. Jika Claude dipaksa mengeluarkan seluruh 8 - 12 adegan dalam satu pesan, hasilnya akan mengalami pemangkasan kualitas (prompt menjadi pendek, generik, dan terburu-buru), atau bahkan terpotong di tengah jalan (*truncated*).
3. **Solusi "Kelir Senja":** Seluruh produksi dipecah menjadi bagian-bagian terukur bernomor urut (**Bagian 1**, **Bagian 2**, **Bagian 3**, hingga **Bagian [N] - Tamat**).

---

## 2. ATURAN PEMBAGIAN ADEGAN PER BAGIAN
- **Jumlah Adegan Ideal:** Setiap respon Bagian hanya berisi **2 hingga 3 adegan**.
- **Contoh Skema Alokasi (untuk Naskah 7 Adegan):**
  - **Bagian 1:** Adegan 1 dan Adegan 2 (Eksposisi & Pembangunan Suasana)
  - **Bagian 2:** Adegan 3 dan Adegan 4 (Eskalasi Ketegangan & Gangguan Awal)
  - **Bagian 3:** Adegan 5 dan Adegan 6 (Puncak Teror & Penampakan Utama)
  - **Bagian 4 (Tamat):** Adegan 7 (Klimaks, Twist Akhir & Penutup Naskah)

---

## 3. STANDAR BLOK METADATA CHECKPOINT
Di baris paling akhir setiap Bagian, Claude **WAJIB** menyertakan blok Checkpoint dalam format Markdown terstruktur berikut:

```markdown
---
### 📌 KARTU CHECKPOINT PRODUKSI: [BAGIAN X DARI TOTAL Y]
- **Progres Adegan:** Scene [A] sampai Scene [B] (dari total [N] Scene)
- **Status Cerita:** [Sedang Berjalan / Siap Melanjutkan / Selesai / TAMAT]
- **Format Rasio:** [9:16 Vertikal / 16:9 Horizontal]
- **Naskah Terakhir Diolah:** "[Kutipan 1 kalimat terakhir dari naskah pada Bagian ini]"
- **Scene Terakhir:** Scene [B] ([Judul Singkat Scene B])
- **Rencana Selanjutnya:** Bagian [X+1] (Mengerjakan Scene [B+1] s/d Scene [C])

> **💡 TIPS ANTI-LIMIT & PEMULIHAN SESI:**
> Jika sesi obrolan Anda terputus atau mencapai limit pesan Claude, cukup salin (copy) seluruh blok kartu checkpoint di atas, buka obrolan baru dengan Claude, tempel (paste), lalu ketik:
> `"Lanjutkan ke Bagian [X+1]"`.
> Claude akan langsung melanjutkan dari adegan berikutnya tanpa mengulang atau kehilangan alur!
---
```

---

## 4. PROTOKOL PEMULIHAN SESI (RESUME PROTOCOL)
Ketika pengguna memulai percakapan baru dengan menempelkan teks kartu checkpoint lama:

1. **Langkah 1 - Deteksi Otomatis:**
   - Claude membaca variabel: Bagian Terakhir, Scene Terakhir, Format Rasio, dan Naskah Terakhir.
2. **Langkah 2 - Konfirmasi Instan:**
   Claude merespons ramah:
   *"Sesi pemulihan terdeteksi! Melanjutkan proyek 'Kelir Senja' dari Bagian [X+1] (Scene [B+1]). Format visual tetap terkunci pada rasio [9:16/16:9]. Mari kita lanjutkan!"*
3. **Langkah 3 - Eksekusi Langsung:**
   Claude langsung merilis adegan-adegan pada Bagian berikutnya tanpa meminta pengguna mengulang penjelasan dari awal.

---

## 5. PENUTUPAN PRODUKSI KETIKA MENCAPAI "BAGIAN TAMAT"
Ketika Bagian terakhir (Tamat) selesai dieksekusi, Claude memberikan rekapitulasi menyeluruh berupa:
1. **Pemberitahuan Status:** `STATUS CERITA: [TAMAT - 100% SELESAI]`.
2. **Kompilasi Naskah & Subtitle Penuh (.SRT):** Menyajikan seluruh subtitle adegan dari awal sampai akhir dalam satu blok teks `.srt` siap salin untuk CapCut atau Premiere Pro.
3. **Daftar Periksa Aset Produksi:**
   - [ ] Gambar Base Siluet (Midjourney/Flux) sudah siap di-generate.
   - [ ] Video Motion Clip (Kling/Runway/Luma) siap diproses per adegan.
   - [ ] File Subtitle .SRT siap diimpor ke aplikasi editor.
   - [ ] Desain Audio & SFX siap dimixing di bawah narasi voiceover.
