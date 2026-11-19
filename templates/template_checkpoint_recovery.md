# TEMPLATE KARTU CHECKPOINT & PEMULIHAN SESI (ANTI-LIMIT)
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

Dokumen ini berisi format standar kartu checkpoint yang digunakan untuk menjaga kelanjutan proyek antar-sesi atau saat kuota pesan Claude terputus.

---

## 1. FORMAT STANDAR KARTU CHECKPOINT (DITEMPELKAN DI AKHIR SETIAP BAGIAN)

```markdown
---
### 📌 KARTU CHECKPOINT PRODUKSI: [BAGIAN X DARI TOTAL Y]
- **Progres Adegan:** Scene [Nomor Awal] s/d Scene [Nomor Akhir] (Total [N] Scene)
- **Status Cerita:** [Sedang Berjalan / Siap Melanjutkan / Selesai / TAMAT]
- **Format Rasio:** [9:16 Vertikal / 16:9 Horizontal]
- **Naskah Terakhir Diolah:** "[Kutipan satu kalimat naskah terakhir yang dibuatkan visualnya]"
- **Scene Terakhir:** Scene [Nomor Akhir] - [Judul Adegan Terakhir]
- **Rencana Selanjutnya:** Bagian [X+1] (Scene [Nomor Berikutnya] s/d Scene [Nomor Target])

> **💡 TIPS ANTI-LIMIT CLAUDE:**
> Jika sesi obrolan Anda terpotong atau kuota pesan Claude habis, cukup salin seluruh blok checkpoint ini.
> Buka sesi obrolan baru dengan Claude, tempelkan blok ini, lalu ketik:
> `"Lanjutkan ke Bagian [X+1]"`.
---
```

---

## 2. CONTOH NYATA PENGGUNAAN PEMULIHAN SESI
Jika Anda sedang mengerjakan sebuah proyek dan terpotong di Bagian 1, cukup kirimkan pesan berikut ke obrolan Claude yang baru:

```text
Halo Claude, saya ingin melanjutkan proyek animasi Kelir Senja yang terpotong. Ini checkpoint terakhir saya:

### 📌 KARTU CHECKPOINT PRODUKSI: BAGIAN 1 DARI TOTAL 3
- Progres Adegan: Scene 1 s/d Scene 2 (Total 6 Scene)
- Status Cerita: Siap Melanjutkan
- Format Rasio: 9:16 Vertikal
- Naskah Terakhir Diolah: "Setiap malam Satu Suro, jendela bilik itu tak pernah boleh dibuka."
- Scene Terakhir: Scene 2 - Jendela Berderit di Malam Buta
- Rencana Selanjutnya: Bagian 2 (Scene 3 s/d Scene 4)

Tolong lanjutkan ke Bagian 2!
```

Claude akan langsung mengenali konteks dan menerbitkan Scene 3 & 4 tanpa mengulang dari awal.
