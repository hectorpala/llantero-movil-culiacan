#!/bin/bash
# Update sitemaps for Llantero Movil Culiacan Pro
# Usage: ./scripts/update-sitemap.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Generating main sitemap..."
python3 "$SCRIPT_DIR/generate-sitemap.py"

echo "Updating sitemap index..."
NOW=$(date -u +"%Y-%m-%dT%H:%M:%S+00:00")
cat > "$PROJECT_DIR/sitemap.xml" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://llanteramovilculiacanpro.mx/sitemaps/main_sitemap.xml</loc>
    <lastmod>$NOW</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://llanteramovilculiacanpro.mx/sitemaps/images_sitemap.xml</loc>
    <lastmod>$NOW</lastmod>
  </sitemap>
</sitemapindex>
EOF

echo "Done! Sitemaps updated."
