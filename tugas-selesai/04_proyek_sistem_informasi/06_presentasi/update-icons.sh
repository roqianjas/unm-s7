#!/bin/bash
# Script untuk mengganti semua SVG icons dengan Iconify icons

for file in slide-*.html; do
  echo "Processing $file..."
  
  # Tambahkan Iconify script jika belum ada
  if ! grep -q "iconify" "$file"; then
    sed -i 's|</head>|    <script src="https://code.iconify.design/2/2.2.1/iconify.min.js"></script>\n</head>|' "$file"
  fi
  
done

echo "Done!"
