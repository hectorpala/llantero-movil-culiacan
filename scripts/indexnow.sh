#!/bin/bash
# IndexNow - Submit URLs to search engines for fast indexing
# Usage: ./scripts/indexnow.sh [url]

DOMAIN="llanteramovilculiacanpro.mx"
KEY_FILE="$(dirname "$0")/../*.txt"

if [ -z "$1" ]; then
  echo "Usage: $0 <url-path>"
  echo "Example: $0 /blog/como-elegir-llantas-correctas/"
  exit 1
fi

URL="https://$DOMAIN$1"
echo "Submitting to IndexNow: $URL"

# Bing/Yandex IndexNow
curl -s -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d "{\"host\":\"$DOMAIN\",\"urlList\":[\"$URL\"]}" || true

echo ""
echo "URL submitted to IndexNow: $URL"
