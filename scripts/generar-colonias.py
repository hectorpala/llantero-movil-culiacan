#!/usr/bin/env python3
"""
Script para generar landing pages de colonias para Llantero Movil Culiacan Pro.
Uso: python3 scripts/generar-colonias.py [bloque_numero]
Ejemplo: python3 scripts/generar-colonias.py 1  # Genera colonias 1-15
"""

import json
import os
import sys

COLONIAS_DIR = "servicios/llantero-colonias-culiacan"
FALTANTES_FILE = "colonias-faltantes.json"
BLOQUE_SIZE = 15

DOMAIN = "https://llanteramovilculiacanpro.mx"
BUSINESS_NAME = "Llantero Movil Culiacan Pro"
WHATSAPP = "526673922273"
PHONE = "667-392-2273"
THEME_COLOR = "#E36414"


def create_slug(nombre):
    slug = nombre.lower()
    replacements = {
        'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
        'n': 'n', ' ': '-', '.': '', ',': '', "'": '', '"': ''
    }
    for old, new in replacements.items():
        slug = slug.replace(old, new)
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    slug = '-'.join(filter(None, slug.split('-')))
    return slug


def generate_html(colonia):
    nombre = colonia['nombre']
    slug = colonia['slug']
    tipo = colonia.get('tipo', 'Colonia')
    tipo_texto = "Fraccionamiento" if tipo == "Fraccionamiento" else "Colonia"
    nombre_enc = nombre.replace(' ', '%20')

    html = f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Llantero Movil en {nombre}, Culiacan | Servicio a Domicilio 24/7</title>
<meta name="description" content="Llantero movil en {tipo_texto} {nombre}, Culiacan. Cambio de llanta, reparacion de ponchadura, vulcanizadora movil a domicilio 24/7. WhatsApp: {PHONE}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png">
<link rel="stylesheet" href="/styles.css">
<link rel="canonical" href="{DOMAIN}/servicios/llantero-colonias-culiacan/{slug}/">
<meta name="theme-color" content="{THEME_COLOR}">
<meta name="geo.region" content="MX-SIN">
<meta name="geo.placename" content="Culiacan">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}/servicios/llantero-colonias-culiacan/{slug}/">
<meta property="og:title" content="Llantero Movil en {nombre}, Culiacan | 24/7">
<meta property="og:description" content="Llantero movil en {tipo_texto} {nombre}. Cambio de llanta, ponchadura, vulcanizado a domicilio. Llegamos en 30-60 min.">
<meta property="og:image" content="{DOMAIN}/assets/images/llantero-movil-hero-1200w.webp">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Inicio","item":"{DOMAIN}/"}},
{{"@type":"ListItem","position":2,"name":"Servicios","item":"{DOMAIN}/#servicios"}},
{{"@type":"ListItem","position":3,"name":"Llantero por Colonias","item":"{DOMAIN}/servicios/llantero-colonias-culiacan/"}},
{{"@type":"ListItem","position":4,"name":"{nombre}","item":"{DOMAIN}/servicios/llantero-colonias-culiacan/{slug}/"}}
]}}
</script>
</head>
<body>
<nav class="nav"><div class="container"><div class="nav-wrapper">
<a href="/" class="logo"><img src="/assets/images/logo-llantero-512.webp" alt="{BUSINESS_NAME}" width="512" height="195"></a>
<button class="mobile-menu-btn" aria-label="Menu"><span></span><span></span><span></span></button>
<ul class="nav-menu"><li><a href="/#inicio" class="nav-link">Inicio</a></li><li><a href="/#servicios" class="nav-link">Servicios</a></li><li><a href="/blog/" class="nav-link">Blog</a></li><li><a href="/#contacto" class="nav-link">Contacto</a></li></ul>
</div></div></nav>

<header id="inicio" class="hero"><div class="container"><div class="hero-content">
<h1 class="fade-in">Llantero Movil en {tipo_texto} {nombre}, Culiacan</h1>
<p class="hero-subtitle fade-in">Servicio de llantero movil a domicilio para residentes de {nombre}. Cambio de llanta, reparacion de ponchadura y vulcanizado. Llegamos en 30-60 minutos.</p>
<a href="https://wa.me/{WHATSAPP}?text=Hola%2C%20necesito%20un%20llantero%20movil%20en%20{nombre_enc}" class="btn-primary hover-lift" target="_blank" rel="noopener noreferrer">Solicitar Llantero Ahora por WhatsApp</a>
</div></div></header>

<section class="section section-alt"><div class="container">
<h2>Por que elegirnos en {nombre}?</h2>
<div class="benefits-grid">
<div class="benefit"><div class="benefit-content"><h3>Conocemos la Zona</h3><p>Experiencia en {tipo_texto.lower()} {nombre} y alrededores</p></div></div>
<div class="benefit"><div class="benefit-content"><h3>Llegada Rapida</h3><p>30-60 minutos en {nombre}</p></div></div>
<div class="benefit"><div class="benefit-content"><h3>Precios Justos</h3><p>Sin sorpresas, cotizacion previa</p></div></div>
<div class="benefit"><div class="benefit-content"><h3>Trabajo Garantizado</h3><p>Garantia en reparaciones y parches</p></div></div>
</div>
</div></section>

<section id="servicios" class="section"><div class="container">
<h2>Servicios de Llantero Movil en {nombre}</h2>
<div class="grid">
<div class="card"><h3>Cambio de Llanta</h3><p>Cambio de llanta ponchada o danada con gato hidraulico profesional.</p></div>
<div class="card"><h3>Reparacion de Ponchadura</h3><p>Parche interno profesional con garantia de 6 meses.</p></div>
<div class="card"><h3>Vulcanizado</h3><p>Vulcanizado profesional a domicilio con equipo portatil.</p></div>
<div class="card"><h3>Inflado y Revision</h3><p>Inflado con compresora industrial y revision de presion.</p></div>
<div class="card"><h3>Alineacion y Balanceo</h3><p>Alineacion y balanceo computarizado de precision.</p></div>
<div class="card"><h3>Emergencias 24/7</h3><p>Servicio las 24 horas, 7 dias, madrugadas y festivos.</p></div>
</div>
</div></section>

<section class="section section-alt"><div class="container">
<h2>Cobertura en {nombre}</h2>
<div class="pricing-content"><div class="pricing-box">
<h3>Atendemos todo el {tipo_texto}</h3>
<p><strong>Llegada rapida:</strong> 30-60 minutos en {nombre}.</p>
<p><strong>Desplazamiento incluido:</strong> Sin costo extra en zona urbana.</p>
<p><strong>Horario:</strong> 24/7 incluyendo madrugadas y festivos.</p>
<p><strong>Garantia:</strong> Todos los trabajos con garantia.</p>
</div></div>
</div></section>

<section class="section"><div class="container">
<h2>Testimonios</h2>
<div class="testimonials">
<div class="testimonial-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Se me poncho la llanta en {nombre} y llegaron en 25 minutos. Rapido y profesional."</p><cite>-- Vecino de {nombre}</cite></div>
<div class="testimonial-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Cambiaron mis llantas a domicilio. Precio justo y buen servicio."</p><cite>-- Cliente en {nombre}</cite></div>
</div>
</div></section>

<section id="contacto" class="section section-alt"><div class="container">
<h2>Necesitas llantero movil en {nombre}?</h2>
<div class="final-cta">
<p class="cta-text">WhatsApp: <strong>{PHONE}</strong></p>
<div class="cta-buttons">
<a href="https://wa.me/{WHATSAPP}?text=Hola%2C%20necesito%20un%20llantero%20en%20{nombre_enc}" target="_blank" rel="noopener noreferrer" class="btn-primary">WhatsApp: {PHONE}</a>
<a href="tel:{PHONE.replace('-','')}" class="btn-secondary">Llamar: {PHONE}</a>
</div>
</div>
</div></section>

<footer class="footer"><div class="container">
<p>&copy; 2026 {BUSINESS_NAME}. Servicio en {nombre}. | <a href="/terminos/">Terminos</a> | <a href="/privacidad/">Privacidad</a></p>
</div></footer>

<a href="https://wa.me/{WHATSAPP}?text=Hola%2C%20necesito%20un%20llantero%20en%20{nombre_enc}" id="cta-whatsapp" class="floating-btn floating-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="Contactar por WhatsApp"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg></a>
<a href="tel:+{WHATSAPP}" id="cta-llamar" class="floating-btn floating-call" aria-label="Llamar ahora"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/></svg></a>
<script src="/main.js" defer></script>
</body>
</html>'''
    return html


def main():
    bloque = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    if not os.path.exists(FALTANTES_FILE):
        print(f"ERROR: No se encontro {FALTANTES_FILE}")
        print('Crea el archivo con formato:')
        print('{"colonias": [{"nombre": "Las Quintas", "slug": "las-quintas", "tipo": "Fraccionamiento"}, ...]}')
        sys.exit(1)

    with open(FALTANTES_FILE, 'r') as f:
        data = json.load(f)

    colonias = data['colonias']
    total = len(colonias)
    start = (bloque - 1) * BLOQUE_SIZE
    end = min(start + BLOQUE_SIZE, total)

    if start >= total:
        print(f"Bloque {bloque} fuera de rango. Total: {total} colonias")
        return

    bloque_colonias = colonias[start:end]
    print(f"Generando Bloque {bloque}: colonias {start+1}-{end} de {total}")
    print("=" * 50)

    created = 0
    for col in bloque_colonias:
        dir_path = os.path.join(COLONIAS_DIR, col['slug'])
        file_path = os.path.join(dir_path, 'index.html')
        if os.path.exists(file_path):
            print(f"  SKIP  {col['nombre']} (ya existe)")
            continue
        os.makedirs(dir_path, exist_ok=True)
        html = generate_html(col)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  OK {col['nombre']} -> {col['slug']}/")
        created += 1

    print("=" * 50)
    print(f"Creadas: {created} | Total en bloque: {len(bloque_colonias)}")
    print(f"\nSiguiente: python3 scripts/generar-colonias.py {bloque + 1}")


if __name__ == "__main__":
    main()
