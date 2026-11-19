# MODUL 07: GENERATOR PROMPT ADEGAN (IMAGE & VIDEO AI)
**Skill:** Kelir Senja Horror Visual System  
**Developer:** Wanz

---

## 1. STRUKTUR MASTER PROMPT "KELIR SENJA"
Setiap prompt adegan yang dihasilkan oleh Claude wajib mengikuti arsitektur baku 6-lapis (*6-Layer Prompt Architecture*):

1. **[Subjek Siluet & Karakter]:** Postur, sosok siluet gelap pekat, busana lokal tradisional, ketiadaan fitur wajah jelas.
2. **[Pencahayaan Hangat Temaram]:** Sumber cahaya diegetik (lampu templok, lilin, obor, bara kemenyan), suhu warna 1800K-2200K, kontras chiaroscuro ekstrem.
3. **[Lingkungan & Properti Otentik]:** Dinding gedhek, bale bambu, sumur tua, rumpun bambu, pohon beringin, tanah becek.
4. **[Atmosfer & Partikel]:** Kabut tanah merayap (*volumetric fog*), asap dupa meliuk, partikel debu melayang dalam berkas cahaya (*dust motes*).
5. **[Sinematografi & Kamera]:** Sudut kamera (low angle, dutch angle, macro), rasio aspect ratio (`--ar 9:16` atau `--ar 16:9`), focal length, kedalaman ruang (*shallow depth of field*).
6. **[Style & Render Engine Keywords]:** Masterclass cinematography, eerie Indonesian horror folklore, dark shadow play aesthetic, photorealistic texture, 8k resolution.

---

## 2. TEMPLATE PROMPT GENERATOR GAMBAR (IMAGE GENERATION)
Cocok untuk: **Midjourney v6.1, Flux.1, Leonardo AI, Stable Diffusion SDXL**.

### Template 9:16 (Vertikal - TikTok / Reels / Shorts):
```text
A chilling Indonesian folklore horror scene, deep pitch-black silhouette of a [NAMA_KARAKTER_MISAL: traditional villager wearing a caping hat], standing motionless in fear, illuminated by a single flickering warm amber oil lamp (lampu templok), 2000K warm golden rim lighting cutting through the darkness, rustic woven bamboo walls (gedhek) with light beams leaking through gaps, [PROPERTI_TAMBAHAN_MISAL: clay water jar and dry leaves on earthen floor], heavy low volumetric fog creeping on the ground, extreme low-angle shot looking up, heavy negative space on the dark top area, cinematic chiaroscuro, photorealistic texture, dark ominous atmosphere, masterclass horror cinematography --ar 9:16 --v 6.1 --style raw
```

### Template 16:9 (Horizontal - YouTube / Sinematik):
```text
A terrifying wide cinematic shot in an ancient Indonesian rural village at midnight, pitch-black silhouette of [NAMA_KARAKTER_MISAL: an ominous tall elongated entity standing near an ancient banyan tree with hanging aerial roots], warm orange glow from a distant bamboo torch flickering against the dense night fog, eerie creaking bamboo grove in background, muddy rural path, rule of thirds composition with wide empty nocturnal landscape, high contrast chiaroscuro shadow play, subtle amber edge highlight, hyper-detailed, eerie silence, 8k resolution, cinematic color grading --ar 16:9 --v 6.1 --style raw
```

### Negative Prompt Rekomendasi:
```text
bright daylight, sunny, neon colors, cartoonish 3D render, generic western monsters, oversaturated, high-key lighting, modern plastic items, clean contemporary clothing, smiling, distorted hands, extra limbs, bad anatomy, text, watermark.
```

---

## 3. TEMPLATE PROMPT GENERATOR VIDEO (VIDEO GENERATION)
Cocok untuk: **Kling AI (v1.5/v2), Runway Gen-3 Alpha, Luma Dream Machine, Minimax Hailuo AI**.

### Panduan Input Video AI:
- **Image-to-Video (I2V - Sangat Direkomendasikan):** Unggah gambar siluet hasil generate di atas, lalu gunakan *motion prompt* untuk menganimasikannya.
- **Text-to-Video (T2V):** Gunakan deskripsi visual + arahan gerak dalam satu kesatuan kalimat.

### Template Motion Prompt:
```text
[CAMERA MOTION]: Slow creeping forward dolly-in camera movement towards the dark figure.
[SUBJECT ACTION]: The pitch-black silhouette stands completely still, holding the antique oil lamp with subtle trembling hands.
[ENVIRONMENT PHYSICS]: The small amber flame flickers organically in the cool nocturnal draft, causing the long shadows on the woven bamboo wall to sway slowly. Ground mist flows lazily across the earthen floor. Wisps of smoke spiral upward into total darkness.
[TONE & PACING]: Ultra-slow horror suspense, smooth continuous movement, high physical accuracy, zero morphing, cinematic 24fps.
```

---

## 4. CONTOH IMPLEMENTASI NYATA PADA ADEGAN

### Skenario: Adegan Penampakan Bayangan di Dinding Bilik (Rasio 9:16)
- **Image Prompt:**
  `Eerie Indonesian horror scene, vertical composition, pitch-black silhouette of a trembling villager sitting on a bamboo bench inside a dark room, illuminated by a melting white candle on a tin plate, casting an enormous grotesque towering shadow on the woven bamboo wall (gedhek) that has elongated unnatural claw-like fingers, warm amber candlelight contrasting with cold nocturnal deep shadows, creeping low fog, cinematic shallow depth of field, high-tension folkloric dread --ar 9:16 --v 6.1`
- **Video Motion Prompt:**
  `Slow zoom in on the human silhouette. The candle flame quivers gently, making the huge demonic shadow on the bamboo wall stretch and slowly tilt its head unnaturally while the human figure remains frozen in terror. Smooth, eerie, cinematic horror pacing, photorealistic shadow dynamics.`
