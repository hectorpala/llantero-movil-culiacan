#!/usr/bin/env python3
"""
Generate main_sitemap.xml for Llantero Movil Culiacan Pro
Scans all index.html files and generates sitemap entries.
"""
import os
import datetime

DOMAIN = "https://llanteramovilculiacanpro.mx"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, "sitemaps", "main_sitemap.xml")

def find_pages(root):
    pages = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs, node_modules, etc
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ('node_modules', 'partials', 'scripts', 'docs', 'css', 'js', 'images')]
        if 'index.html' in filenames:
            rel = os.path.relpath(dirpath, root)
            if rel == '.':
                url = '/'
            else:
                url = '/' + rel.replace(os.sep, '/') + '/'
            # Skip gracias page
            if '/gracias/' in url:
                continue
            pages.append(url)
    return sorted(pages)

def generate_sitemap(pages):
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+00:00')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        priority = '1.0' if page == '/' else '0.8' if '/servicios/' in page else '0.6'
        changefreq = 'weekly' if page == '/' or '/servicios/' in page else 'monthly'
        xml += f'  <url>\n'
        xml += f'    <loc>{DOMAIN}{page}</loc>\n'
        xml += f'    <lastmod>{now}</lastmod>\n'
        xml += f'    <changefreq>{changefreq}</changefreq>\n'
        xml += f'    <priority>{priority}</priority>\n'
        xml += f'  </url>\n'
    xml += '</urlset>\n'
    return xml

if __name__ == '__main__':
    pages = find_pages(ROOT)
    print(f"Found {len(pages)} pages")
    sitemap = generate_sitemap(pages)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"Sitemap written to {OUTPUT}")
