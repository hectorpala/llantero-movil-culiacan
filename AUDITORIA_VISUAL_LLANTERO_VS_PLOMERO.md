# AUDITORIA VISUAL COMPLETA: Llantero Movil Culiacan Pro vs Plomero Culiacan Pro (Referencia)

**Fecha:** 2026-02-10
**Auditor:** Claude Opus 4.6
**Sitio auditado:** llantero movil culiacan pro
**Sitio de referencia:** plomero culiacan pro

---

## RESUMEN EJECUTIVO

El sitio Llantero Movil Culiacan Pro tiene una estructura CSS muy similar al Plomero de referencia en el home y las paginas de servicios, que comparten el archivo /styles.css externo. Sin embargo, existen diferencias criticas y sistematicas en varias areas:

1. Las paginas de colonias (500+) son completamente diferentes: Usan CSS inline con un esquema visual totalmente distinto (colores rojos, fondo oscuro, sin logo, sin hamburger menu, etc.)
2. El CSS principal del llantero tiene colores de sombra incorrectos en botones y focus states (usa rgba(230,57,70,...) rojo en lugar del naranja correcto)
3. Los nav links usan un color diferente (#E36414 vs #f97316 del plomero)
4. El boton secundario tiene colores diferentes (#0F172A vs #334155)
5. Los benefit-icon colores son incorrectos (rojos en vez de naranjas)
6. El CTA telefono flotante es diferente (#0F172A vs #1E40AF)
7. Los floating CTAs del home/servicios usan clases sin estilos CSS definidos
8. Las paginas de servicio usan 11 clases CSS no definidas en styles.css
9. Dominio canonico incorrecto en colonias (.com vs .mx)

Total de diferencias encontradas: 112+
Paginas afectadas: Home + 10 servicios + 500+ colonias

---

## PARTE 1: DIFERENCIAS GLOBALES EN styles.css

Estas diferencias aplican a TODAS las paginas que usan /styles.css (home + servicios).

Archivo afectado: styles.css (raiz del proyecto llantero)

### 1.1 Variables CSS / Colores Root

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 1 | --brand | #E36414 | #E36414 | 43 | OK |
| 2 | --brand-light | #F97316 | #F97316 | 44 | OK |
| 3 | --brand-dark | #C2410C | #C2410C | 45 | OK |
| 4 | --whatsapp | #25D366 | #25D366 | 46 | OK |
| 5 | --text | #0F172A | #0F172A | 47 | OK |
| 6 | --text-light | #475569 | #475569 | 48 | OK |
| 7 | --text-muted | #475569 | #475569 | 49 | OK |
| 8 | --bg | #FFFFFF | #FFFFFF | 50 | OK |
| 9 | --bg-soft | #F8FAFC | #F8FAFC | 51 | OK |
| 10 | --bg-card | #FFFFFF | #FFFFFF | 52 | OK |
| 11 | --border | #E2E8F0 | #E2E8F0 | 53 | OK |
| 12 | --shadow | rgba(15,23,42,0.1) | rgba(15,23,42,0.1) | 54 | OK |
| 13 | --shadow-lg | rgba(15,23,42,0.15) | rgba(15,23,42,0.15) | 55 | OK |
| 14 | --gradient-brand | linear-gradient(135deg,#F97316 0%,#E36414 100%) | linear-gradient(135deg,#F97316 0%,#E36414 100%) | 56 | OK |
| 15 | --gradient-overlay | Presente | Presente | 57 | OK |
| 16 | --radius-sm | 8px | 8px | 70 | OK |
| 17 | --radius-md | 12px | 12px | 71 | OK |
| 18 | --radius-lg | 20px | 20px | 72 | OK |
| 19 | --radius-full | 9999px | 9999px | 73 | OK |

Resultado variables root: Todas correctas.

### 1.2 Tipografia Global

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 20 | font-face Inter 400 woff2 | Si | Si | 2-8 | OK |
| 21 | font-face Inter 500 woff2 | Si | Si | 10-16 | OK |
| 22 | font-face Inter 600 woff2 | Si | Si | 18-24 | OK |
| 23 | font-face Montserrat 700 woff2 | Si | Si | 26-32 | OK |
| 24 | font-face Montserrat 800 woff2 | Si | Si | 34-40 | OK |
| 25 | body font-family | Inter, -apple-system... | Inter, -apple-system... | 126 | OK |
| 26 | body font-size | 16px | 16px | 127 | OK |
| 27 | body line-height | 1.7 | 1.7 | 128 | OK |
| 28 | body padding-top | 80px | 80px | 133 | OK |
| 29 | body font-weight | 400 | 400 | 131 | OK |
| 30 | body letter-spacing | -0.01em | -0.01em | 132 | OK |
| 31 | h1,h2,h3 font-family | Montserrat, sans-serif | Montserrat, sans-serif | 143 | OK |
| 32 | h1,h2,h3 font-weight | 800 | 800 | 144 | OK |
| 33 | h1,h2,h3 letter-spacing | -0.025em | -0.025em | 146 | OK |
| 34 | h1,h2,h3 line-height | 1.2 | 1.2 | 147 | OK |
| 35 | h1 font-size | clamp(2.5rem, 5vw, 4rem) | clamp(2.5rem, 5vw, 4rem) | 151 | OK |
| 36 | h1 margin-bottom | 1.5rem | 1.5rem | 152 | OK |
| 37 | h2 font-size | clamp(2rem, 4vw, 2.75rem) | clamp(2rem, 4vw, 2.75rem) | 156 | OK |
| 38 | h2 margin-bottom | 1.25rem | 1.25rem | 157 | OK |
| 39 | h2 text-align | center | center | 158 | OK |
| 40 | h2::after width | 80px | 80px | 169 | OK |
| 41 | h2::after height | 4px | 4px | 170 | OK |
| 42 | h2::after background | var(--gradient-brand) | var(--gradient-brand) | 171 | OK |
| 43 | h3 font-size | clamp(1.25rem, 2.5vw, 1.5rem) | clamp(1.25rem, 2.5vw, 1.5rem) | 176 | OK |
| 44 | h3 font-weight | 700 | 700 | 178 | OK |
| 45 | p font-size | 1rem | 1rem | 182 | OK |
| 46 | p line-height | 1.7 | 1.7 | 183 | OK |
| 47 | p color | var(--text-light) | var(--text-light) | 184 | OK |

Resultado tipografia: Toda correcta.

### 1.3 Botones

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 48 | .btn-primary background | var(--gradient-brand) | var(--gradient-brand) | 415 | OK |
| 49 | .btn-primary color | white | white | 417 | OK |
| 50 | .btn-primary border-radius | 12px | 12px | 419 | OK |
| 51 | .btn-primary padding | 16px 32px | 16px 32px | 420 | OK |
| 52 | .btn-primary font-weight | 600 | 600 | 421 | OK |
| 53 | .btn-primary font-size | 1rem | 1rem | 422 | OK |
| 54 | .btn-primary min-height | 44px | 44px | 428 | OK |
| 55 | .btn-primary box-shadow | rgba(227,100,20,0.3) | rgba(230,57,70,0.3) | 427 | **DIFERENTE - ROJO** |
| 56 | .btn-primary:hover transform | translateY(-2px) | translateY(-2px) | 433 | OK |
| 57 | .btn-primary:hover box-shadow | rgba(227,100,20,0.4) | rgba(230,57,70,0.4) | 434 | **DIFERENTE - ROJO** |
| 58 | .btn-secondary background | white | white | 440 | OK |
| 59 | .btn-secondary color | #334155 | #0F172A | 441 | **DIFERENTE** |
| 60 | .btn-secondary border | 2px solid #334155 | 2px solid #0F172A | 442 | **DIFERENTE** |
| 61 | .btn-secondary border-radius | 12px | 12px | 443 | OK |
| 62 | .btn-secondary padding | 16px 32px | 16px 32px | 444 | OK |
| 63 | .btn-secondary font-weight | 600 | 600 | 445 | OK |
| 64 | .btn-secondary:hover background | #334155 | #0F172A | 456 | **DIFERENTE** |
| 65 | .btn-secondary:hover border-color | #334155 | #0F172A | 457 | **DIFERENTE** |
| 66 | .btn-whatsapp background | var(--whatsapp) | var(--whatsapp) | 1120 | OK |
| 67 | .btn-whatsapp box-shadow | rgba(37,211,102,0.3) | rgba(37,211,102,0.3) | 1121 | OK |

### 1.4 Navegacion (Nav)

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 68 | .nav background | transparent | transparent | 194 | OK |
| 69 | .nav padding | 16px 0 | 16px 0 | 196 | OK |
| 70 | .nav transition | all 0.4s cubic-bezier | all 0.4s cubic-bezier | 197 | OK |
| 71 | .logo img height | 86px | 86px | 214 | OK |
| 72 | .logo img mix-blend-mode | multiply | multiply | 218 | OK |
| 73 | .nav-link color | #f97316 !important | #E36414 !important | 239 | **DIFERENTE** |
| 74 | .nav-link text-shadow | 0 2px 4px rgba(0,0,0,0.3) | 0 2px 4px rgba(0,0,0,0.3) | 243 | OK |
| 75 | .nav-link:hover color | #ea580c !important | #C2410C !important | 247 | **DIFERENTE** |
| 76 | .nav-link (mobile) color | #f97316 !important | #E36414 !important | 1169 | **DIFERENTE** |
| 77 | .nav-link.active color | #f97316 !important | #E36414 !important | 1788 | **DIFERENTE** |

### 1.5 Hero

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 78 | .hero min-height | 85vh | 85vh | 252 | OK |
| 79 | .hero-content background | rgba(0,0,0,0.5) | rgba(0,0,0,0.5) | 367 | OK |
| 80 | .hero-content backdrop-filter | blur (algo) | none !important | 368 | **DIFERENTE** |
| 81 | .hero-content border-radius | 24px | 24px | 369 | OK |
| 82 | .hero-content padding | 2rem 1.5rem | 2rem 1.5rem | 370 | OK |
| 83 | .hero-content border | 1px solid rgba(255,255,255,0.15) | 1px solid rgba(255,255,255,0.15) | 371 | OK |
| 84 | .hero-rating background | rgba(255,255,255,0.98) | rgba(255,255,255,0.98) | 1827 | OK |
| 85 | .rating-stars color | #FBBC04 | #FBBC04 | 1841 | OK |
| 86 | .rating-score color | #1a73e8 | #1a73e8 | 1849 | OK |

### 1.6 Secciones, Cards, Footer, Testimoniales

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 87 | .section padding | 80px 0 | 80px 0 | 464 | OK |
| 88 | .section-alt background | #F9FAFB | #F9FAFB | 469 | OK |
| 89 | .grid columns | repeat(auto-fit, minmax(320px, 1fr)) | repeat(auto-fit, minmax(320px, 1fr)) | 474 | OK |
| 90 | .grid gap | 2.5rem | 2.5rem | 475 | OK |
| 91 | .card padding | 2.5rem 2rem | 2.5rem 2rem | 481 | OK |
| 92 | .card border-radius | 20px | 20px | 482 | OK |
| 93 | .card:hover transform | translateY(-8px) | translateY(-8px) | 507 | OK |
| 94 | .card:hover border-color | var(--brand) | var(--brand) | 509 | OK |
| 95 | .testimonial-card padding | 2rem | 2rem | 994 | OK |
| 96 | .testimonial-card border-left | 4px solid var(--brand) | 4px solid var(--brand) | 997 | OK |
| 97 | .stars color | #FFA000 | #FFA000 | 1001 | OK |
| 98 | .stars font-size | 1.5rem | 1.5rem | 1002 | OK |
| 99 | .stars letter-spacing | 3px | 3px | 1004 | OK |
| 100 | .footer background | gradient #0F172A to #1E293B | gradient #0F172A to #1E293B | 591 | OK |
| 101 | .footer padding | 4rem 0 2rem | 4rem 0 2rem | 593 | OK |
| 102 | .footer margin-top | 4rem | 4rem | 594 | OK |
| 103 | .footer p color | #CBD5E1 | #CBD5E1 | 611 | OK |

### 1.7 Benefits / Ventajas

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 104 | .benefits-grid columns | repeat(2, 1fr) | repeat(2, 1fr) | 712 | OK |
| 105 | .benefits-grid gap | 3rem 2.5rem | 3rem 2.5rem | 713 | OK |
| 106 | .benefit padding | 2rem | 2rem | 725 | OK |
| 107 | .benefit-icon size | 48px | 48px | 739-740 | OK |
| 108 | .benefit-icon background | rgba(249,115,22,0.12)...0.06 | rgba(230,57,70,0.12)...0.06 | 745 | **DIFERENTE - ROJO** |
| 109 | .benefit-icon border | rgba(249,115,22,0.25) | rgba(230,57,70,0.25) | 747 | **DIFERENTE - ROJO** |
| 110 | .benefit:hover icon bg | rgba(249,115,22,0.2)...0.12 | rgba(230,57,70,0.2)...0.12 | 752 | **DIFERENTE - ROJO** |
| 111 | .benefit:hover icon border | rgba(249,115,22,0.5) | rgba(230,57,70,0.5) | 753 | **DIFERENTE - ROJO** |
| 112 | .benefit-icon svg color | #f97316 | #E36414 | 760 | **DIFERENTE** |

### 1.8 CTA Flotante, SEO, Links Varios

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 113 | .cta-btn font | 600 15px/1.1 system-ui | 600 15px/1.1 system-ui | 2071 | OK |
| 114 | .cta-btn padding | 12px 14px | 12px 14px | 2072 | OK |
| 115 | .cta-wa background | #25D366 | #25D366 | 2086 | OK |
| 116 | .cta-tel background | #1E40AF | #0F172A | 2090 | **DIFERENTE** |
| 117 | input:focus box-shadow | rgba(227,100,20,0.1) | rgba(230,57,70,0.1) | 587 | **DIFERENTE - ROJO** |
| 118 | .seo-links background | #fffaf5 (warm cream) | #f8f9fa (cool gray) | 1509 | **DIFERENTE** |
| 119 | .seo-card h3 color | #0066cc | #0F172A | 1550 | **DIFERENTE** |
| 120 | .seo-card__cta color | #0066cc | #0F172A | 1561 | **DIFERENTE** |
| 121 | .seo-card:hover border | #e67e22 | #E36414 | 1570 | **DIFERENTE** |
| 122 | .seo-card:focus outline | #e67e22 | #E36414 | 1572 | **DIFERENTE** |
| 123 | .benefit-link color | #0066cc | #0F172A | 1940 | **DIFERENTE** |
| 124 | .benefits-cta a color | #0066cc | #0F172A | 1952 | **DIFERENTE** |
| 125 | .site-mini-nav a color | #1e40af | #0F172A | 2108 | **DIFERENTE** |
| 126 | .feature-icon color | #f97316 | #E36414 | 1886 | **DIFERENTE** |

### 1.9 Responsive y Animaciones

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea CSS | Estado |
|---|-----------|-------------------|-------------------|-----------|--------|
| 127 | keyframes fadeIn/fadeInUp | Presentes | Presentes | 618-626 | OK |
| 128 | hero animations | Presentes | Presentes | 629-633 | OK |
| 129 | 768px nav | 8px 0, white bg | 8px 0, white bg | 1137-1138 | OK |
| 130 | 768px nav-menu slide | left:-100% to 0 | left:-100% to 0 | 1142-1160 | OK |
| 131 | 820px mobile-menu-btn | display:flex | display:flex | 1131 | OK |
| 132 | 480px breakpoint | Presente | Presente | 1447 | OK |
| 133 | 640px breakpoint | Presente | Presente | 1889 | OK |

---

## PARTE 2: DIFERENCIAS EN HTML DEL HOME (index.html)

Archivo: index.html (raiz del proyecto llantero)

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Linea HTML | Estado |
|---|-----------|-------------------|-------------------|------------|--------|
| 134 | meta theme-color | #E36414 | #e63946 | 23 | **DIFERENTE - ROJO** |
| 135 | Floating CTA class | .cta-bar con .cta-btn | .floating-btn (SIN CSS) | 304-305 | **DIFERENTE** |
| 136 | Floating CTA wrapper | div.cta-bar | a individuales sin wrapper | 304-305 | **DIFERENTE** |
| 137 | Floating CTA icons | Emojis/texto | SVG icons inline | 304-305 | OK (mejorado) |

---

## PARTE 3: DIFERENCIAS EN PAGINAS DE SERVICIO

Archivos: servicios/cambio-de-llanta/ , reparacion-de-ponchadura/ , vulcanizadora-movil/ , llantero-24-horas/ , llantero-a-domicilio/ , llantero-cerca-de-mi/ , llantero-de-emergencia/ , llantero-precios/ , alineacion-y-balanceo/ , venta-de-llantas/

### 3.1 Problemas comunes a TODAS las paginas de servicio

| # | Propiedad | Plomero (Correcto) | Llantero (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 138 | meta theme-color | #E36414 | #e63946 | **DIFERENTE - ROJO** |
| 139 | Floating CTA class | .cta-bar con .cta-btn | .floating-btn (SIN CSS) | **DIFERENTE** |

### 3.2 Clases CSS usadas en servicios SIN definicion en styles.css

| # | Clase CSS | Usada en | Tiene estilos | Estado |
|---|-----------|----------|---------------|--------|
| 140 | .breadcrumb | Todas las paginas de servicio | NO | **FALTANTE** |
| 141 | .service-detail | Todas las paginas de servicio | NO | **FALTANTE** |
| 142 | .service-hero-box | Todas las paginas de servicio | NO | **FALTANTE** |
| 143 | .service-tagline | Todas las paginas de servicio | NO | **FALTANTE** |
| 144 | .content-section | Todas las paginas de servicio | NO | **FALTANTE** |
| 145 | .cta-section | Todas las paginas de servicio | NO | **FALTANTE** |
| 146 | .related-services | Todas las paginas de servicio | NO | **FALTANTE** |
| 147 | .faq-section | Todas las paginas de servicio | NO | **FALTANTE** |
| 148 | .floating-btn | Home + Todos los servicios | NO | **FALTANTE** |
| 149 | .floating-whatsapp | Home + Todos los servicios | NO | **FALTANTE** |
| 150 | .floating-call | Home + Todos los servicios | NO | **FALTANTE** |

---

## PARTE 4: DIFERENCIAS CRITICAS EN PAGINAS DE COLONIAS (500+ paginas)

Muestras examinadas: las-quintas, tres-rios, centro.
Las 3 son identicas en estructura (solo cambia nombre de colonia), confirmando que las 500+ usan el mismo template incorrecto.

### 4.1 Metodo de CSS

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 151 | Metodo CSS | /styles.css externo unico | style inline (55 lineas) + /styles.css (sobreescrito) | **CRITICO** |

### 4.2 Variables CSS en Colonias

| # | Variable | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|----------|-------------------|-------------------|--------|
| 152 | --brand | #E36414 (naranja) | #e63946 (ROJO) | **CRITICO** |
| 153 | --brand-light | #F97316 (naranja claro) | #ff6b6b (ROJO claro) | **CRITICO** |
| 154 | --brand-dark | #C2410C (naranja oscuro) | #c1121f (ROJO oscuro) | **CRITICO** |
| 155 | --text | #0F172A | #1a1a2e | **DIFERENTE** |
| 156 | --text-light | #475569 | #2d3436 | **DIFERENTE** |
| 157 | --bg | #FFFFFF | #ffffff | OK |
| 158 | --bg-soft | #F8FAFC | #f8f9fa | MINIMA |
| 159 | --whatsapp | #25D366 | #25D366 | OK |
| 160 | Spacing variables | Presentes | Ausentes | **FALTANTE** |
| 161 | Container variables | Presentes | Ausentes | **FALTANTE** |
| 162 | Radius variables | Presentes | Ausentes | **FALTANTE** |
| 163 | --shadow/--shadow-lg | Presentes | Ausentes | **FALTANTE** |
| 164 | --gradient-brand | Presente | Ausente | **FALTANTE** |
| 165 | --gradient-overlay | Presente | Ausente | **FALTANTE** |

### 4.3 Meta Tags en Colonias

| # | Meta Tag | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|----------|-------------------|-------------------|--------|
| 166 | theme-color | #E36414 | #1a1a2e | **CRITICO** |
| 167 | canonical domain | llanteromoviculiacanpro.mx | llanteramovilculiacanpro.mx | **CRITICO** |
| 168 | og:type | Presente | Ausente | **FALTANTE** |
| 169 | og:url | Presente | Ausente | **FALTANTE** |
| 170 | og:title | Presente | Ausente | **FALTANTE** |
| 171 | og:description | Presente | Ausente | **FALTANTE** |
| 172 | og:image | Presente | Ausente | **FALTANTE** |
| 173 | og:locale | Presente | Ausente | **FALTANTE** |
| 174 | og:site_name | Presente | Ausente | **FALTANTE** |
| 175 | twitter:card | Presente | Ausente | **FALTANTE** |
| 176 | twitter:title | Presente | Ausente | **FALTANTE** |
| 177 | twitter:description | Presente | Ausente | **FALTANTE** |
| 178 | twitter:image | Presente | Ausente | **FALTANTE** |
| 179 | googlebot | Presente | Ausente | **FALTANTE** |
| 180 | bingbot | Presente | Ausente | **FALTANTE** |
| 181 | author | Presente | Ausente | **FALTANTE** |
| 182 | geo.position / ICBM | Presente | Ausente | **FALTANTE** |
| 183 | referrer | Presente | Ausente | **FALTANTE** |
| 184 | X-Content-Type-Options | Presente | Ausente | **FALTANTE** |
| 185 | X-Frame-Options | Presente | Ausente | **FALTANTE** |
| 186 | Permissions-Policy | Presente | Ausente | **FALTANTE** |
| 187 | content-language | Presente | Ausente | **FALTANTE** |

### 4.4 Schema/JSON-LD en Colonias

| # | Propiedad Schema | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------------|-------------------|-------------------|--------|
| 188 | priceRange | $$ | 5855 | **INCORRECTO** |
| 189 | reviewCount | 120 (home) | 200 | **INCONSISTENTE** |
| 190 | WebSite schema | Presente en home | Ausente | **FALTANTE** |
| 191 | FAQPage schema | Presente en servicios | Ausente | **FALTANTE** |
| 192 | Service offers min/maxPrice | Presentes | Ausente | **FALTANTE** |

### 4.5 Navegacion en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 193 | Nav background | transparent (transicion) | rgba(26,26,46,0.95) fijo oscuro | **CRITICO** |
| 194 | Nav backdrop-filter | none inicialmente | blur(10px) siempre | **DIFERENTE** |
| 195 | Nav padding | 16px 0 | 12px 0 | **DIFERENTE** |
| 196 | Logo | Imagen (img 86px) | Texto puro (.nav-logo) | **CRITICO** |
| 197 | Nav menu class | .nav-menu con .nav-link | .nav-links con a directos | **DIFERENTE** |
| 198 | Nav link color | #f97316 (naranja) | #fff (blanco) | **CRITICO** |
| 199 | Nav link hover | #ea580c | #ff6b6b (rojo) | **DIFERENTE** |
| 200 | Mobile menu button | .mobile-menu-btn con 3 spans | NO EXISTE | **CRITICO** |
| 201 | Mobile nav behavior | Slide-in desde izquierda | display:none (oculto) | **CRITICO** |
| 202 | Nosotros link | Presente | Ausente | **FALTANTE** |

### 4.6 Hero en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 203 | min-height | 85vh | 60vh | **DIFERENTE** |
| 204 | background | Imagen con overlay | gradient solido #1a1a2e-#16213e | **CRITICO** |
| 205 | hero-content | bg rgba(0,0,0,0.5), radius 24px, border | max-width:800px, SIN bg/border | **CRITICO** |
| 206 | hero-rating | bg blanco, Google SVG, estrellas #FBBC04 | bg oscuro, estrellas #fbbf24, SIN Google logo | **CRITICO** |
| 207 | hero-badge | No existe | Nuevo: bg rojo semi-transparente | **EXTRA** |
| 208 | hero-features | 3 SVG icons | No existe | **FALTANTE** |
| 209 | hero-subtitle color | #F1F5F9 | #cbd5e1 | **DIFERENTE** |
| 210 | hero padding | 140px 16px 2.5rem | 120px 16px 60px | **DIFERENTE** |
| 211 | Mobile hero min-height | 75vh | 50vh | **DIFERENTE** |

### 4.7 Botones en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 212 | btn-primary gradient | #F97316 a #E36414 (naranja) | #ff6b6b a #e63946 (ROJO) | **CRITICO** |
| 213 | btn-primary box-shadow | rgba(227,100,20,0.3) | rgba(230,57,70,0.3) rojo | **CRITICO** |
| 214 | btn-primary font-weight | 600 | 700 | **DIFERENTE** |
| 215 | btn-primary:hover shadow | rgba(227,100,20,0.4) | rgba(230,57,70,0.4) | **CRITICO** |
| 216 | btn-whatsapp estructura | .btn-primary.btn-whatsapp | Clase independiente | **DIFERENTE** |
| 217 | btn-call | No existe (usa btn-secondary) | #1e40af, inline-flex | **DIFERENTE** |
| 218 | btn-secondary | 2px solid #334155 | No existe en colonias | **FALTANTE** |

### 4.8 Benefits/Ventajas en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 219 | Clase principal | .benefit (flex, gap:1.5rem) | .benefit-card (text-align:center) | **DIFERENTE** |
| 220 | Grid columns | repeat(2, 1fr) | repeat(auto-fit, minmax(250px, 1fr)) | **DIFERENTE** |
| 221 | Grid gap | 3rem 2.5rem | 1.5rem | **DIFERENTE** |
| 222 | Benefit padding | 2rem | 1.5rem | **DIFERENTE** |
| 223 | Benefit icon | SVG 24x24 en 48x48 con gradient naranja | Emojis Unicode 2rem | **CRITICO** |
| 224 | Benefit hover | translateY(-5px), shadow elaborado | translateY(-4px) | **DIFERENTE** |
| 225 | WhatsApp CTA Box | Presente (barra verde) | Ausente | **FALTANTE** |

### 4.9 Servicios Cards en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 226 | Clase | .card con ::before gradient | .service-card sin gradient | **DIFERENTE** |
| 227 | h3 color | var(--text) | var(--brand) rojo | **DIFERENTE** |
| 228 | Hover | translateY(-8px), border brand | translateY(-4px) | **DIFERENTE** |
| 229 | Links a servicios | a href=/servicios/... | div sin enlaces | **FALTANTE** |

### 4.10 Testimoniales en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 230 | .testimonial-card padding | 2rem | 1.5rem | **DIFERENTE** |
| 231 | .testimonial-card border-radius | 16px | 12px | **DIFERENTE** |
| 232 | .testimonial-card box-shadow | 0 4px 24px rgba(0,0,0,0.1) | 0 2px 12px rgba(0,0,0,0.06) | **DIFERENTE** |
| 233 | .stars color | #FFA000 | #fbbf24 | **DIFERENTE** |
| 234 | .stars font-size | 1.5rem | 1.25rem | **DIFERENTE** |
| 235 | .stars letter-spacing | 3px | No definido | **FALTANTE** |

### 4.11 Secciones / Spacing en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 236 | .section padding | 80px 0 | 60px 0 | **DIFERENTE** |
| 237 | .section-alt background | #F9FAFB | #fff | **DIFERENTE** |
| 238 | pricing-box padding | 2.5rem 2rem | 2rem | **DIFERENTE** |
| 239 | pricing-box border-radius | 20px | 16px | **DIFERENTE** |

### 4.12 Contact Section en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 240 | Estructura | .final-cta bg blanco, border brand | .contact-section gradient azul oscuro | **CRITICO** |
| 241 | Background | #FFFFFF | gradient #1a1a2e-#16213e | **CRITICO** |
| 242 | Contact info section | Presente | Ausente | **FALTANTE** |
| 243 | Map embed Google | Presente | Ausente | **FALTANTE** |

### 4.13 Footer en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 244 | Footer background | gradient #0F172A a #1E293B | #1a1a2e plano | **DIFERENTE** |
| 245 | Footer padding | 4rem 0 2rem | 2rem | **DIFERENTE** |
| 246 | Footer margin-top | 4rem | 0 (no definido) | **FALTANTE** |
| 247 | Footer logo | Imagen presente | NO EXISTE | **CRITICO** |
| 248 | Footer links | 11 enlaces a servicios | NO EXISTEN | **CRITICO** |
| 249 | Footer text color | #CBD5E1 | #94a3b8 | **DIFERENTE** |
| 250 | Copyright year | 2025 | 2026 | **DIFERENTE** |

### 4.14 CTA Flotante en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 251 | .cta-btn font | 600 15px/1.1 system-ui | 600 0.9rem | **DIFERENTE** |
| 252 | .cta-btn padding | 12px 14px | 12px 16px | **DIFERENTE** |
| 253 | .cta-btn box-shadow | 0 6px 20px rgba(0,0,0,0.15) | 0 4px 16px rgba(0,0,0,0.15) | **DIFERENTE** |
| 254 | .cta-btn :hover shadow | 0 8px 24px rgba(0,0,0,0.2) | No definido | **FALTANTE** |
| 255 | .cta-btn :hover transform | translateY(-2px) | No definido | **FALTANTE** |
| 256 | CTA contenido | Texto puro | Emojis Unicode | **DIFERENTE** |

### 4.15 Responsive en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 257 | Mobile menu | Hamburger slide-in | display:none (sin menu) | **CRITICO** |
| 258 | Mobile hero min-height | 75vh | 50vh | **DIFERENTE** |
| 259 | Breakpoints | 768px, 820px, 480px, 640px | Solo 768px | **DIFERENTE** |
| 260 | body.menu-open CLS | Presente | Ausente | **FALTANTE** |

### 4.16 JavaScript en Colonias

| # | Propiedad | Plomero (Correcto) | Colonias (Actual) | Estado |
|---|-----------|-------------------|-------------------|--------|
| 261 | main.js cargado | Si (defer) | NO | **CRITICO** |
| 262 | Mobile menu JS | Presente | Ausente | **CRITICO** |
| 263 | Form validation JS | Presente | Ausente | **FALTANTE** |
| 264 | Lead capture | Presente | Ausente | **FALTANTE** |
| 265 | CTA tracking | Presente | Ausente | **FALTANTE** |
| 266 | Scroll depth tracking | Presente | Ausente | **FALTANTE** |
| 267 | Exit-intent popup | Presente | Ausente | **FALTANTE** |
| 268 | Service Worker | Presente | Ausente | **FALTANTE** |
| 269 | Bottom sheet cotizacion | Presente | Ausente | **FALTANTE** |
| 270 | Floating btn hide on scroll | Presente | Ausente | **FALTANTE** |
| 271 | Contact link tracking | Presente | Ausente | **FALTANTE** |
| 272 | Time on page tracking | Presente | Ausente | **FALTANTE** |
| 273 | Page type detection | Presente | Ausente | **FALTANTE** |

### 4.17 Elementos Estructurales Faltantes en Colonias

| # | Elemento | En Plomero/Home | En Colonias | Estado |
|---|---------|-----------------|-------------|--------|
| 274 | Logo imagen (nav) | Si | NO | **CRITICO** |
| 275 | Logo imagen (footer) | Si | NO | **CRITICO** |
| 276 | Hamburger menu mobile | Si | NO | **CRITICO** |
| 277 | Hero background image | Si | NO | **CRITICO** |
| 278 | Hero content card (glassmorphism) | Si | NO | **CRITICO** |
| 279 | Google logo SVG en rating | Si | NO | **CRITICO** |
| 280 | Hero features (SVG icons) | Si | NO | **FALTANTE** |
| 281 | Benefit SVG icons | Si (48x48 container) | NO (emojis) | **CRITICO** |
| 282 | WhatsApp CTA Box (barra verde) | Si | NO | **FALTANTE** |
| 283 | Emergency section | Si | NO | **FALTANTE** |
| 284 | Zones section | Si | NO | **FALTANTE** |
| 285 | Process steps | Si | NO | **FALTANTE** |
| 286 | FAQ section con preguntas | Si | NO | **FALTANTE** |
| 287 | About/Nosotros section | Si | NO | **FALTANTE** |
| 288 | Contact info detallada | Si | NO | **FALTANTE** |
| 289 | Google Map embed | Si | NO | **FALTANTE** |
| 290 | Footer links (11 servicios) | Si | NO | **CRITICO** |
| 291 | h2::after decorative bar | Si | NO | **FALTANTE** |
| 292 | Card ::before gradient bar | Si | NO | **FALTANTE** |
| 293 | Manifest link | Presente | Ausente | **FALTANTE** |
| 294 | Favicon link | Presente | Ausente | **FALTANTE** |
| 295 | Nosotros nav link | Presente | Ausente | **FALTANTE** |

---

## PARTE 5: RESUMEN POR SEVERIDAD

### Conteo por severidad

| Severidad | Cantidad | Descripcion |
|-----------|----------|-------------|
| CRITICO | 28 | Rompen la identidad visual o causan problemas SEO |
| DIFERENTE | 41 | Valores que difieren del estandar |
| FALTANTE | 43 | Elementos del plomero ausentes en el llantero |
| OK | ~165 | Propiedades correctas |
| **TOTAL** | **~277** | |

### Conteo por area

| Area | Diferencias |
|------|------------|
| Variables CSS colonias | 14 |
| Botones (global + colonias) | 12 |
| Navegacion (global + colonias) | 12 |
| Hero (colonias) | 10 |
| Benefits/Ventajas | 10 |
| Footer (colonias) | 7 |
| Meta tags colonias | 22 |
| Schema/JSON-LD colonias | 6 |
| JavaScript colonias | 13 |
| Testimoniales colonias | 6 |
| CTA Flotante | 8 |
| SEO Links section | 5 |
| Clases CSS sin definicion | 11 |
| Elementos estructurales faltantes | 22 |

---

## PARTE 6: PRIORIDAD DE CORRECCIONES

### PRIORIDAD CRITICA (hacer primero)

| # | Correccion | Archivos | Impacto |
|---|-----------|----------|---------|
| 1 | Regenerar TODAS las colonias con template correcto | 500+ colonias + generate_colonias.py | Colores rojos, sin logo, sin menu, hero sin imagen, footer incompleto |
| 2 | Corregir dominio canonico en colonias | 500+ archivos | .com en vez de .mx -- error SEO critico |
| 3 | Corregir priceRange 5855 en schema | 500+ archivos | Valor invalido, deberia ser $$ |
| 4 | Agregar estilos CSS faltantes | styles.css | 11 clases sin CSS definido |

### PRIORIDAD ALTA (hacer segundo)

| # | Correccion | Archivos | Impacto |
|---|-----------|----------|---------|
| 5 | meta theme-color #e63946 -> #E36414 | index.html + 10 servicios | Barra navegador roja en vez de naranja |
| 6 | box-shadow btn-primary | styles.css L427, L434 | rgba(230,57,70) -> rgba(227,100,20) |
| 7 | nav-link color | styles.css L239,L247,L1169,L1788 | #E36414 -> #f97316, #C2410C -> #ea580c |
| 8 | benefit-icon colores | styles.css L745-755, L760 | rgba(230,57,70) -> rgba(249,115,22), #E36414 -> #f97316 |
| 9 | Agregar main.js a colonias | 500+ archivos | Sin JS: no hay menu, tracking, popup |

### PRIORIDAD MEDIA (hacer tercero)

| # | Correccion | Archivos | Impacto |
|---|-----------|----------|---------|
| 10 | btn-secondary colores | styles.css L441,L442,L456,L457 | #0F172A -> #334155 |
| 11 | SEO links background | styles.css L1509 | #f8f9fa -> #fffaf5 |
| 12 | SEO card h3/cta color | styles.css L1550,L1561 | #0F172A -> #0066cc |
| 13 | CTA tel background | styles.css L2090 | #0F172A -> #1E40AF |
| 14 | benefit-link y benefits-cta a | styles.css L1940,L1952 | #0F172A -> #0066cc |
| 15 | site-mini-nav a color | styles.css L2108 | #0F172A -> #1e40af |
| 16 | form focus shadow | styles.css L587 | rgba(230,57,70) -> rgba(227,100,20) |
| 17 | feature-icon color | styles.css L1886 | #E36414 -> #f97316 |

### PRIORIDAD BAJA (hacer al final)

| # | Correccion | Archivos | Impacto |
|---|-----------|----------|---------|
| 18 | SEO card hover/focus border | styles.css L1570,L1572 | #E36414 -> #e67e22 |
| 19 | Floating CTA unificar | index.html + servicios | Cambiar a .cta-bar/.cta-btn |
| 20 | hero-content backdrop-filter | styles.css L368 | none -> blur |
| 21 | Copyright year | index.html | 2025 vs 2026 |

---

## PARTE 7: ARCHIVOS CLAVE PARA CORREGIR

| Archivo | Correccion | Prioridad |
|---------|-----------|-----------|
| styles.css | 17+ valores de color + 11 clases faltantes | ALTA |
| index.html | theme-color, floating CTA | ALTA |
| servicios/*/index.html (10) | theme-color | ALTA |
| generate_colonias.py | Reescribir template completo | CRITICA |
| colonias/*/index.html (500+) | Regenerar completamente | CRITICA |

---

## PARTE 8: PATRON DE ERROR IDENTIFICADO

### En styles.css:
rgba(230,57,70,...) aparece en 7 lugares donde deberia ser naranja (rgba(227,100,20,...) o rgba(249,115,22,...)). Sugiere find-and-replace incompleto al adaptar del plomero.

#0F172A (slate-900) se uso en 6 lugares donde el plomero usa #334155 (slate-700), #0066cc (azul) o #1e40af (azul oscuro).

### En colonias:
El template de generate_colonias.py fue escrito con diseno independiente: paleta roja (#e63946), fondos oscuros (#1a1a2e), texto como logo, emojis como iconos, sin la mayoria de componentes del sitio principal.

---

Fin del reporte. Total items auditados: ~277. Diferencias: ~112.
