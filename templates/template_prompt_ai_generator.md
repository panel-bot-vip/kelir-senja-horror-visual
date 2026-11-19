# LEMBAR FORMULA PROMPT GENERATOR (IMAGE & VIDEO AI)
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

Dokumen ini adalah panduan praktis perakitan prompt untuk generator gambar (Midjourney, Flux, Leonardo) dan generator video (Kling AI, Runway Gen-3, Luma Dream Machine) sesuai pakem "Kelir Senja".

---

## 1. BANK KATA KUNCI BAKU (VOCABULARY BANK)

### A. Karakter Siluet & Entitas
- `pitch-black silhouette of a terrified Indonesian villager`: Siluet hitam pekat warga desa yang ketakutan.
- `dark shadowy figure standing in unnatural stiff posture`: Sosok bayangan berdiri dengan postur kaku tak wajar.
- `ominous tall elongated humanoid silhouette with thin claw-like fingers`: Siluet humanoid jangkung membungkuk dengan jari kurus menyerupai cakar.
- `shrouded silhouette figure lingering in deep darkness`: Sosok siluet berbalut kain (pocong) membeku di kegelapan.
- `floating silhouette of a long-haired female entity`: Siluet melayang sosok perempuan berambut panjang menjuntai.

### B. Pencahayaan Hangat Temaram (Warm Amber)
- `illuminated by a single flickering traditional oil lamp (lampu templok)`: Disinari lampu minyak teplok tradisional yang berkedip.
- `warm amber candlelight glowing 2000K`: Cahaya lilin hangat kekuningan 2000 Kelvin.
- `casting long, jittery, exaggerated shadows on woven bamboo walls`: Memproyeksikan bayangan panjang yang bergetar di dinding anyaman bambu.
- `golden rim lighting carving the edge of the dark silhouette`: Garis cahaya tepi keemasan mempertegas siluet gelap.
- `extreme chiaroscuro lighting, deep black shadows contrasting with warm orange glow`: Pencahayaan chiaroscuro ekstrem, bayangan hitam kontras dengan cahaya jingga.

### C. Properti & Arsitektur Lokal
- `rustic woven bamboo wall (gedhek) with light beams piercing through tiny slits`: Dinding anyaman bambu dengan berkas cahaya menembus celah kecil.
- `creaking bamboo bench (bale-bale) on earthen floor`: Bale bambu berderit di atas lantai tanah liat.
- `weathered mossy stone water well with wooden pulley in the dark backyard`: Sumur tua berlumut dengan kerekan kayu di pekarangan belakang yang gelap.
- `incense smoke curling slowly into the cold night air`: Asap dupa meliuk perlahan di udara malam yang dingin.

### D. Lingkungan Alam & Atmosfer
- `dense misty bamboo grove creaking in the nocturnal breeze`: Rumpun bambu berkabut lebat berderit ditiup angin malam.
- `ancient banyan tree with hanging aerial roots`: Pohon beringin kuno dengan akar gantung menjuntai.
- `creeping volumetric ground fog rolling across muddy path`: Kabut tanah volumetrik merayap di atas jalan setapak becek.

---

## 2. POLA PERAKITAN PROMPT GAMBAR (IMAGE PROMPT PATTERN)
```text
[Kategori Scene & Nuansa Horor] + [Subjek Siluet & Gestur] + [Sumber Pencahayaan Hangat & Rim Light] + [Properti Lokal & Dinding Bambu] + [Atmosfer Kabut & Lingkungan] + [Komposisi Kamera & Rasio]
```

### Contoh Hasil Jadi:
```text
A haunting Indonesian folklore horror scene, pitch-black silhouette of a traditional villager sitting frozen on an old bamboo bench, illuminated by a melting candle in a tin plate, warm amber 2000K edge lighting, huge terrifying shadow with clawed hands cast upon the rustic woven bamboo wall (gedhek), low creeping fog on earthen floor, low-angle shot, cinematic chiaroscuro, photorealistic texture, 8k resolution --ar 9:16 --v 6.1 --style raw
```

---

## 3. POLA PERAKITAN MOTION PROMPT VIDEO (VIDEO MOTION PATTERN)
```text
[ARAHAN KAMERA]: Slow creeping forward dolly-in / subtle pan across the room.
[GERAKAN SUBJEK]: The dark silhouette stands motionless with barely noticeable heavy breathing.
[FISIKA LINGKUNGAN]: The warm amber oil lamp flame flickers organically in the cool breeze, making the ominous shadow on the bamboo wall sway and stretch subtly. Ground mist rolls slowly across the floor.
[RITME & KUALITAS]: Extremely slow horror tension, cinematic pacing, smooth continuous motion, zero distortion, 24fps.
```
