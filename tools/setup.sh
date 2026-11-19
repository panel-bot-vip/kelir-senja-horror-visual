#!/usr/bin/env bash
# Setup Kelir Senja Environment by Wanz
set -e
echo "Memeriksa dependensi Kelir Senja Horror Visual Kit..."
which ffmpeg >/dev/null || (echo "ERROR: ffmpeg belum terinstall" && exit 1)
which python3 >/dev/null || (echo "ERROR: python3 belum terinstall" && exit 1)
python3 -c "import PIL, numpy" >/dev/null || (echo "ERROR: Pillow dan numpy belum terinstall. Jalankan: pip install pillow numpy" && exit 1)
chmod +x tools/*.py 2>/dev/null || true
echo "Semua dependensi lengkap! Kelir Senja Animation Engine siap digunakan."
