#!/usr/bin/env bash
# Zkopíruje webovou část do add-onu (addon/www), aby se dala zabalit do image.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf addon/www
mkdir -p addon/www/data
cp index.html addon/www/
cp manifest.webmanifest icon.svg sw.js addon/www/
cp data/songs.js addon/www/data/
echo "addon/www: $(find addon/www -type f | wc -l) souborů"
