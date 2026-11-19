# MODUL 04: DINAMIKA ANIMASI, GERAKAN & PACING HOROR
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

---

## 1. FILOSOFI GERAKAN: "THE CREEPING DREAD"
Dalam animasi horor folklor bernuansa siluet gelap, kengerian tidak dibangun dari gerakan aksi yang cepat dan gaduh, melainkan dari **ketenangan yang menekan (oppressive stillness)** dan **gerakan mikro yang janggal (uncanny micro-movements)**.

### Karakteristik Ritme Animasi:
1. **Ritme Lambat Bertekanan (Slow Pacing):** 70% adegan didominasi gerakan lambat, hening, dan terukur. Karakter bergerak berhati-hati, menahan napas, atau terpaku dalam ketakutan.
2. **Koreografi Api & Bayangan (Shadow Choreography):** Ketika subjek utama berdiri diam mematung, api lentera berkedip lembut, membuat siluet bayangan di dinding bergoyang dan meregang secara independen.
3. **Gerakan Tak Wajar Entitas Gaib (Uncanny Motion):** Makhluk gaib tidak bergerak seperti manusia biasa. Gerakannya bisa berupa:
   - Melayang lambat tanpa langkah kaki (*weightless gliding*).
   - Gerakan patah-patah (*stuttering / stop-motion style twitching*) pada leher atau jari.
   - Posisi kepala yang miring perlahan ke sudut yang mustahil (45° hingga 90°).

---

## 2. ANATOMI GERAKAN SEKUNDER (SECONDARY MOTION)
Agar animasi AI tidak terkesan kaku (*rigid* atau *static freeze*), setiap adegan wajib menyertakan elemen gerakan sekunder:

- **Asap Dupa / Kemenyan:** Gumpalan asap putih tipis berputar-putar perlahan (*slow wisps of smoke swirling*), naik ke langit-langit bambu dan perlahan memudar di kegelapan.
- **Kain & Serat Pakaian:** Ujung sarung batik lusuh atau kain mori putih yang berkibar pelan ditiup angin malam basah (*cloth blowing in gentle nocturnal breeze*).
- **Rambut Basah Terurai:** Helai rambut panjang yang bergerak halus seperti melayang di dalam air.
- **Dedaunan & Batang Alam:** Batang-batang bambu yang saling bergesekan (*groaning bamboo poles*), daun pisang robek yang melambai pelan di luar jendela.
- **Kabut Tanah (Ground Mist):** Kabut putih pekat yang merayap di atas tanah becek (*creeping volumetric low fog*).

---

## 3. FORMULA KEMUNCULAN HOROR: "STILLNESS BEFORE THE SNAP"
Gunakan struktur 3 fase ini dalam mengarahkan pergerakan adegan penampakan:

1. **Fase Hening (Detik 0 - 2):**
   - Karakter siluet terpaku kaku. Hanya ada gerakan api lampu minyak yang mengecil dan kepulan napas dingin.
   - Suara malam mendadak lenyap (jangkrik berhenti berderik).
2. **Fase Curiga (Detik 2 - 3.5):**
   - Bayangan di dinding mulai memanjang secara mandiri, atau siluet kepala di kegelapan perlahan memiring ke samping.
   - Gerakan kamera melakukan *slow creeping dolly-in*.
3. **Fase Hentakan Halus / Reveal (Detik 3.5 - 5):**
   - Bukan sekadar ledakan jumpscare murahan, melainkan gerakan mendadak yang dingin: tangan kurus dengan kuku panjang mencengkeram kusen pintu, atau pendar mata samar tiba-tiba menyala di tengah bayangan pekat.

---

## 4. PANDUAN MOTION PROMPT UNTUK AI VIDEO ENGINES (KLING, RUNWAY, LUMA)
Untuk menghasilkan gerakan yang mulus dan bebas distorsi aneh (*morphing artifacts*), gunakan prinsip deskripsi gerak berikut:

- **Gunakan Kata Kerja Presisi:** Hindari kata ambigu seperti *"moves around"*. Gunakan *"slowly turns its head to the left"*, *"subtle trembling hands"*, *"flickering flame casting jittery shadows"*, *"creeping slow forward camera movement"*.
- **Batasi Magnitude Gerakan:** Jaga parameter gerakan (*motion intensity*) pada tingkat rendah-sedang (skala 3 - 5 dari 10). Horor siluet memerlukan ketenangan artistik yang mencekam, bukan aksi akrobatik.

### Formula Motion Prompt Baku:
```text
Slow, eerie, continuous motion. The dark silhouette of the human figure stands motionless, holding an antique oil lamp. The small amber flame flickers organically in the night breeze, casting swaying elongated shadows on the woven bamboo wall behind. Low fog creeps along the earthen floor. Cinematic slow push-in camera movement. Realistic physics, high suspense, moody atmospheric pacing, no jitter, no warping.
```
