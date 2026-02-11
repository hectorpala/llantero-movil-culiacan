# ESTRUCTURA DE REFERENCIA - Plomero Culiacan Pro
## Documento para replicar exactamente en Llantero Movil Culiacan Pro

---

## 1. ESTRUCTURA DE DIRECTORIOS

```
plomero culiacan pro/
+-- index.min.html          # Homepage principal (minificada, ~89KB)
+-- styles.css              # CSS completo (2282 lineas)
+-- styles.min.css          # CSS minificado
+-- main.js                 # JavaScript principal (826 lineas)
+-- manifest.json           # PWA manifest
+-- sw.js                   # Service Worker
+-- robots.txt              # Config robots
+-- sitemap.xml             # Sitemap index
+-- netlify.toml            # Config Netlify (headers, cache, redirects)
+-- favicon.ico             # Favicon principal
+-- CNAME                   # Dominio personalizado
+-- .nojekyll               # Deshabilitar Jekyll
+-- assets/
|   +-- fonts/ (inter-400/500/600.woff2, montserrat-700/800.woff2)
|   +-- icons/ (favicons, apple-touch-icons, icon-72 to icon-512, logo-blue.svg)
|   +-- images/ (hero-*-800w/1200w.webp, service images, social-proof/)
+-- partials/
|   +-- cta.html            # CTA flotante (WhatsApp + Llamar)
|   +-- faq_precios.html    # FAQ section con schema
|   +-- footer_nav.html     # Mini footer navigation
|   +-- gtm.html            # Google Tag Manager snippet
|   +-- jsonld_base.html    # JSON-LD schemas base
+-- servicios/              # 17+ carpetas de servicio + colonias (645+)
+-- blog/                   # Blog con articulos
+-- contacto/               # Pagina de contacto
+-- gracias/                # Thank you page (noindex)
+-- privacidad/             # Politica de privacidad
+-- terminos/               # Terminos y condiciones
+-- sitemaps/
    +-- main_sitemap.xml
    +-- images_sitemap.xml
```

---

## 2. INDEX.MIN.HTML - ESTRUCTURA HEAD COMPLETA

### 2.1 Meta Tags

```html
<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Plomero en Culiacan 24/7 | Llegada en 30-60 min + Garantia</title>
<meta name="description" content="Plomero certificado en Culiacan...">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="googlebot" content="index, follow">
<meta name="bingbot" content="index, follow">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
<meta http-equiv="Permissions-Policy" content="geolocation=(), microphone=(), camera=()">
<meta http-equiv="content-language" content="es-MX">
<meta name="geo.region" content="MX-SIN">
<meta name="geo.placename" content="Culiacan">
<meta name="geo.position" content="24.7903;-107.3878">
<meta name="ICBM" content="24.7903, -107.3878">
<!-- Favicons: icon 16/32/192/512, apple-touch 180/152/144/128/96/72 -->
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#0066cc">
<!-- Preconnect: googletagmanager, wa.me, google.com, fonts.googleapis.com -->
<!-- Preload: hero image (srcset 800w+1200w), 5 fonts woff2 -->
<!-- Critical CSS inline: @font-face + :root vars + above-fold styles -->
<!-- External CSS: preload async pattern -->
<!-- Canonical + hreflang (es-mx, es, x-default) -->
<!-- OG tags (type, url, title, description, image 800x800, locale, site_name) -->
<!-- Twitter Card (summary_large_image) -->
<meta name="x-build" content="ISO_DATE">
```

### 2.2 JSON-LD Schema @graph (en HEAD)

Contiene un UNICO bloque script type="application/ld+json" con @graph:

1. **WebSite** - nombre, url, logo, SearchAction
2. **BreadcrumbList** - Inicio
3. **Organization** - nombre, url, logo, telefono, email, address, sameAs, contactPoint
4. **HomeAndConstructionBusiness** (para llantero: AutoRepair)
   - nombre, url, telefono, address, horarios 24/7
   - areaServed: 30+ colonias como Place
   - sameAs: Google My Business, Facebook, Instagram
   - logo, image, geo (lat/lng)
   - priceRange: "$$", paymentAccepted, currenciesAccepted: MXN
   - aggregateRating: 4.8/5, 150 reviews
   - 6 reviews con autor, fecha, texto, rating, publisher Google, image
5. **Service** (uno por cada servicio, ~6 servicios)
   - serviceType, name, description, provider ref
   - areaServed: City Culiacan en Sinaloa
   - image con ImageObject
   - offers con PriceSpecification (minPrice/maxPrice MXN)
   - serviceOutput (opcional)
6. **FAQPage** - 7+ preguntas con Question/Answer

### 2.3 BODY - Secciones en Orden

```
1.  GTM Script (requestIdleCallback diferido)
2.  GTM noscript iframe
3.  NAV fija (.nav > .container > .nav-wrapper)
    - .logo > img (512x195 webp)
    - .mobile-menu-btn (hamburger 3 spans)
    - ul.nav-menu: Inicio, Servicios, Sobre Nosotros, Blog, Contacto
4.  HEADER#inicio .hero
    - picture.hero-background (srcset 800w+1200w webp, fetchpriority high)
    - .hero-content (glassmorphism card)
      - h1 principal
      - .hero-rating (Google badge: SVG logo + stars + 4.8/5 + 150+ reviews)
      - p.hero-subtitle
      - .hero-features (3-4 items con SVG icons)
      - .hero-contact (telefono)
      - .hero-guarantee
      - a.btn-primary (WhatsApp CTA)
5.  SECTION "Por que elegirnos"
    - .benefits-grid (2 cols desktop)
      - 4x .benefit (icon + h3 + p + .benefit-list)
      - .whatsapp-cta-box (CTA verde full-width)
    - .benefits-cta
6.  SECTION#servicios "Nuestros Servicios"
    - .grid auto-fit
      - a.card.card--img (6-8 service cards)
        - .service-card > .media-box > img
        - h3, p, .service-cta
    - p.services-intro (SEO text)
7.  SECTION#colonias-destacadas "Servicio por Colonia"
    - Grid de colonias con links
    - .all-colonies-link
8.  SECTION .seo-links "Mas opciones"
    - .seo-grid (1/2/3 cols responsive)
      - a.seo-card (con data-event tracking)
    - .seo-links__note
9.  SECTION "Urgencias 24/7"
    - .emergency-content: h2 + texto + btn WhatsApp
10. SECTION "Zonas de Servicio"
    - .zones-content: h2 + lista colonias
11. SECTION "Precios Transparentes"
    - .pricing-box con precios y CTA
12. SECTION "Nuestro Proceso"
    - .process-steps: 4 pasos (numero + h3 + p)
13. SECTION "Preguntas Frecuentes"
    - .faq: details/summary items
14. SECTION#sobre-nosotros "Sobre Nosotros"
    - .about-content + .features grid
15. SECTION#noticias "Blog"
    - .news-grid: .news-card (image + date + h3 + p + read-more)
16. SECTION "Testimonios"
    - .testimonial-grid: .testimonial-card (stars + quote + cite)
    - .testimonials-cta
17. SECTION .social-proof "Prueba Real"
    - .google-reviews-grid (review screenshots)
    - .team-showcase (team photos)
    - .before-after-gallery (before/after images)
18. SECTION#contacto
    - .contact-content (2 cols)
      - .contact-info (tel, whatsapp, horario, zona)
      - form#contact-form (nombre, telefono, email, mensaje, submit)
19. SECTION "Directorio" (links SEO adicionales)
20. .final-cta (box con 2 botones: WhatsApp + Llamar)
21. FOOTER .footer (logo + copyright)
22. CTA flotante .cta-bar (WhatsApp + Llamar, position:fixed)
23. MINI FOOTER NAV nav.site-mini-nav
24. EXIT INTENT POPUP #exit-intent-popup
25. NOSCRIPT fallback
26. script src="main.js" defer
```

---

## 3. CSS - SISTEMA DE DISENO

### 3.1 Variables :root

```css
:root {
  --brand: #E36414;           /* Naranja principal */
  --brand-light: #F97316;     /* Naranja claro */
  --brand-dark: #C2410C;
  --whatsapp: #25D366;
  --text: #0F172A;
  --text-light: #475569;
  --text-muted: #475569;
  --bg: #FFFFFF;
  --bg-soft: #F8FAFC;
  --bg-card: #FFFFFF;
  --border: #E2E8F0;
  --shadow: rgba(15,23,42,0.1);
  --shadow-lg: rgba(15,23,42,0.15);
  --gradient-brand: linear-gradient(135deg,#F97316 0%,#E36414 100%);
  --gradient-overlay: linear-gradient(135deg,rgba(15,23,42,0.9) 0%,rgba(30,41,59,0.8) 100%);
  --space-xs: 0.5rem; --space-sm: 1rem; --space-md: 2rem; --space-lg: 3rem; --space-xl: 4rem;
  --container-max-width: 1200px;
  --container-gutter: 24px;
  --radius-sm: 8px; --radius-md: 12px; --radius-lg: 20px; --radius-full: 9999px;
}
```

### 3.2 Tipografia
- Headings: Montserrat 700-800, letter-spacing: -0.025em
- Body: Inter 400-600, 16px, line-height: 1.7
- h1: clamp(2.5rem, 5vw, 4rem)
- h2: clamp(2rem, 4vw, 2.75rem) + 80px gradient underline
- h3: clamp(1.25rem, 2.5vw, 1.5rem)

### 3.3 Breakpoints
- 480px (small mobile), 640px (mobile), 768px (tablet/main), 820px (large tablet)
- min-width 769px (desktop), 1200px (large desktop)

### 3.4 Clases Principales
| Clase | Uso |
|-------|-----|
| .container | Max-width 1200px centered |
| .section | Padding 80px 0, scroll-margin-top 120px |
| .grid | Auto-fit minmax(320px, 1fr) |
| .card / .card--img | Cards con border, shadow, hover lift |
| .btn-primary | Naranja gradient, hover translateY(-2px) |
| .btn-secondary | Blanco con borde |
| .btn-whatsapp | Verde WhatsApp |
| .hero | Background image, min-height 85vh |
| .hero-content | Glassmorphism card (backdrop-filter blur) |
| .hero-rating | Pill badge Google rating |
| .nav | Fixed top, z-index 50 |
| .cta-bar | Fixed bottom-right (WhatsApp+Llamar) |
| .benefits-grid | 2 cols, benefit cards |
| .whatsapp-cta-box | Green CTA box full-width |
| .faq-item | details/summary accordion |
| .testimonial-card | Review card con stars |
| .social-proof | Google reviews + team + before/after |
| .seo-grid / .seo-card | SEO internal link cards |
| .service-card + .media-box | Service image card |
| .footer | Dark gradient background |
| .site-mini-nav | Inline link nav |
| .exit-popup-* | Exit intent modal |
| .fade-in | fadeIn animation |

---

## 4. MAIN.JS - 12 MODULOS

1. **Mobile Menu**: open/close hamburger, scroll preservation, aria
2. **Form Validation**: real-time (nombre 2+chars, tel 10 digits, email regex, mensaje 10+chars)
3. **Lead Capture**: GA4 dataLayer + localStorage + Netlify Forms + WhatsApp redirect
4. **CTA Tracking**: floating buttons dataLayer events
5. **Footer Nav Tracking**: nav_click events
6. **SEO Card Tracking**: click_seo_card events (requestIdleCallback)
7. **Scroll Depth**: 25/50/75/90% milestones (rAF throttle)
8. **Exit Intent Popup**: desktop mouseleave / mobile 30s timer + back button
9. **Service Worker**: register /sw.js
10. **Quote Bottom Sheet**: mobile chip selection, swipe-to-close, focus trap
11. **Hide Floating Buttons**: IntersectionObserver on contact/footer sections
12. **Extra Tracking**: tel/wa links, time-on-page milestones, internal nav, page type

---

## 5. MANIFEST.JSON

```json
{
  "name": "NOMBRE - Servicio 24/7",
  "short_name": "CORTO",
  "description": "...",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0066cc",
  "orientation": "portrait-primary",
  "scope": "/",
  "lang": "es-MX",
  "dir": "ltr",
  "icons": [192px png/webp, 512px png/webp, logo webp],
  "categories": ["business", "utilities"],
  "shortcuts": [WhatsApp emergency, Llamar]
}
```

---

## 6. ROBOTS.TXT
- Allow all except /gracias/, /admin/, /private/
- Allow Googlebot, Googlebot-Image, Facebook, Twitter
- Block AhrefsBot, SemrushBot, MJ12bot, DotBot
- Sitemap references

## 7. SITEMAP.XML
- Sitemap index pointing to main_sitemap.xml + images_sitemap.xml

## 8. SW.JS
- Cache-First for assets, Network-First for HTML, Network-only for forms

## 9. NETLIFY.TOML
- Security headers (X-Frame-Options, nosniff, XSS, Referrer)
- HTML: no cache; Images/CSS/JS/Fonts: 1yr immutable; Sitemap: 24h
- 404 redirect

---

## 10. PAGINAS DE SERVICIO

### Head
- Title SEO optimizado con servicio + ciudad + frase conversion
- Meta description con emoji al inicio
- Meta keywords long-tail
- Canonical URL absoluta
- Mismos favicons, preconnects, fonts, critical CSS inline
- JSON-LD @graph: WebSite + BreadcrumbList + Business + Services + FAQPage

### Body (misma estructura que homepage)
- GTM (diferido 2000ms post-load)
- NAV identica
- HERO identico (misma imagen, H1 unico por servicio)
- 4 beneficios especificos del servicio
- Servicios grid (todos los servicios)
- Colonias, SEO links, Urgencias, Zonas, Precios, Proceso, FAQ, About, Blog, Testimonios, Social Proof, Contacto form, Final CTA, Footer, CTA flotante, Mini nav, Exit popup
- main.js defer

### Internal Linking
- Links a TODOS los demas servicios
- Links a colonias
- Links a blog, contacto, homepage

---

## 11. DATOS NEGOCIO PLOMERO (REFERENCIA)

| Campo | Valor |
|-------|-------|
| Nombre | Plomero Culiacan Pro |
| Dominio | plomeroculiacanpro.mx |
| Telefono | +52 667 392 2273 |
| WhatsApp | 526673922273 |
| Email | contacto@plomeroculiacanpro.mx |
| Ciudad | Culiacan |
| Estado | Sinaloa |
| Coords | 24.7903, -107.3878 |
| Rating | 4.8/5 (150+ reviews) |
| Horario | 24/7 |
| Theme | #0066cc |
| Brand | #E36414 (naranja) |
| GTM | GTM-W75CRTX5 |
| Schema | HomeAndConstructionBusiness |

---

## 12. EQUIVALENCIAS PLOMERO -> LLANTERO

| Plomero | Llantero |
|---------|----------|
| HomeAndConstructionBusiness | AutoRepair |
| Plumber | TireShop / AutoRepair |
| plomero | llantero |
| plomeria | servicios de llantas |
| fugas | ponchadura |
| destape drenajes | cambio de llanta |
| instalacion boiler | balanceo y alineacion |
| instalacion tinaco | venta de llantas |
| reparacion sanitarios | rotacion de llantas |
| emergencia plomeria | auxilio vial |
| /servicios/plomero-* | /servicios/llantero-* |

---

FIN DEL DOCUMENTO DE REFERENCIA
