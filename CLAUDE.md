# Llantero Móvil Culiacán Pro

## Sobre el proyecto
- Sitio web estático (HTML/CSS/JS) para negocio local de llantas en Culiacán, Sinaloa
- Enfoque principal: SEO local y Google My Business
- Hospedado en GitHub Pages con dominio personalizado (ver CNAME)
- Repo: github.com/hectorpala

## Estructura
- `/index.html` — Página principal
- `/blog/` — 6 artículos SEO sobre llantas
- `/servicios/` — 11 páginas de servicios (llantero 24h, vulcanizadora, alineación, etc.)
- `/contacto/` — Formulario de contacto
- `/partials/` — Componentes reutilizables (header, footer, GTM)
- `/images/` — Imágenes del sitio
- `/css/`, `/js/` — Estilos y scripts

## MCP configurados
- Playwright — Para auditorías visuales del sitio (abrir, navegar, screenshots)

## Pendientes
- Configurar MCP de Google Search Console (requiere credenciales de Google Cloud)
  1. Crear proyecto en Google Cloud Console
  2. Activar Search Console API
  3. Crear cuenta de servicio y descargar JSON
  4. Agregar email de servicio como admin en Search Console
  5. Agregar config al settings.json

## Notas
- El estilo y formato sigue el estándar del proyecto hermano "plomero culiacan pro"
- Responder siempre en español
- GTM se inyecta automáticamente via partials
