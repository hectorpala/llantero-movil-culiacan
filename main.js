// Main JavaScript - Llantera Movil Culiacan Pro
// Loaded with defer for optimal performance
// Last updated: 2026-02-10

// Mobile menu toggle with scroll position preservation
(function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    if (!mobileMenuBtn || !navMenu) return;

    let scrollY = 0;

    function openMenu() {
        scrollY = window.scrollY;
        document.body.style.top = '-' + scrollY + 'px';
        document.body.classList.add('menu-open');
        navMenu.classList.add('active');
        mobileMenuBtn.classList.add('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
        mobileMenuBtn.setAttribute('aria-label', 'Cerrar menu de navegacion');
    }

    function closeMenu() {
        const savedScrollY = scrollY;
        document.body.classList.remove('menu-open');
        document.body.style.top = '';
        navMenu.classList.remove('active');
        mobileMenuBtn.classList.remove('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.setAttribute('aria-label', 'Abrir menu de navegacion');
        window.scrollTo(0, savedScrollY);
    }

    mobileMenuBtn.addEventListener('click', () => {
        if (document.body.classList.contains('menu-open')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
})();

// Real-time form validation
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const nombreField = document.getElementById('nombre');
    const telefonoField = document.getElementById('telefono');
    const emailField = document.getElementById('email');
    const mensajeField = document.getElementById('mensaje');
    const submitBtn = form.querySelector('button[type="submit"]');

    const validators = {
        nombre: (value) => value.trim().length >= 2,
        telefono: (value) => /^[0-9]{10}$/.test(value.replace(/\s/g, '')),
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        mensaje: (value) => value.trim().length >= 10
    };

    function validateField(field, validatorKey) {
        const value = field.value;
        const fieldWrapper = field.closest('.form-field');
        const isValid = validators[validatorKey](value);

        if (value.length === 0) {
            fieldWrapper.classList.remove('valid', 'invalid');
        } else if (isValid) {
            fieldWrapper.classList.remove('invalid');
            fieldWrapper.classList.add('valid');
        } else {
            fieldWrapper.classList.remove('valid');
            fieldWrapper.classList.add('invalid');
        }

        updateSubmitButton();
        return isValid;
    }

    function isFormValid() {
        return validators.nombre(nombreField.value) &&
               validators.telefono(telefonoField.value) &&
               validators.email(emailField.value) &&
               validators.mensaje(mensajeField.value);
    }

    function updateSubmitButton() {
        if (isFormValid()) {
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            submitBtn.style.cursor = 'pointer';
        } else {
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';
            submitBtn.style.cursor = 'not-allowed';
        }
    }

    nombreField.addEventListener('input', () => validateField(nombreField, 'nombre'));
    nombreField.addEventListener('blur', () => validateField(nombreField, 'nombre'));

    telefonoField.addEventListener('input', () => {
        telefonoField.value = telefonoField.value.replace(/\D/g, '');
        validateField(telefonoField, 'telefono');
    });
    telefonoField.addEventListener('blur', () => validateField(telefonoField, 'telefono'));

    emailField.addEventListener('input', () => validateField(emailField, 'email'));
    emailField.addEventListener('blur', () => validateField(emailField, 'email'));

    mensajeField.addEventListener('input', () => validateField(mensajeField, 'mensaje'));
    mensajeField.addEventListener('blur', () => validateField(mensajeField, 'mensaje'));

    updateSubmitButton();
})();

// Multi-layer lead capture: Netlify Forms + localStorage + GA4 + WhatsApp
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const nombre = formData.get('nombre');
        const telefono = formData.get('telefono');
        const email = formData.get('email');
        const mensaje = formData.get('mensaje');

        const leadData = {
            timestamp: new Date().toISOString(),
            nombre: nombre,
            telefono: telefono,
            email: email,
            mensaje: mensaje,
            source: 'homepage_form',
            url: window.location.href
        };

        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'generate_lead',
                'form_name': 'contact_form_homepage',
                'method': 'netlify_forms',
                'value': 1,
                'currency': 'MXN'
            });
        }

        try {
            const leads = JSON.parse(localStorage.getItem('llantero_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('llantero_leads', JSON.stringify(leads));
        } catch (e) {}

        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            });

            if (response.ok) {
                const whatsappMessage = 'Hola! Necesito servicio de llantera a domicilio:\n\n' +
                                      'Nombre: ' + nombre + '\n' +
                                      'Telefono: ' + telefono + '\n' +
                                      'Email: ' + email + '\n' +
                                      'Mensaje: ' + mensaje;
                const whatsappURL = 'https://wa.me/526673922273?text=' + encodeURIComponent(whatsappMessage);

                window.open(whatsappURL, '_blank');
                window.location.href = '/gracias';
            } else {
                throw new Error('Netlify form submission failed');
            }
        } catch (error) {
            alert('Formulario enviado. Te redirigiremos a WhatsApp.');
            const whatsappMessage = 'Hola! Necesito servicio de llantera a domicilio:\n\n' +
                                  'Nombre: ' + nombre + '\n' +
                                  'Telefono: ' + telefono + '\n' +
                                  'Email: ' + email + '\n' +
                                  'Mensaje: ' + mensaje;
            const whatsappURL = 'https://wa.me/526673922273?text=' + encodeURIComponent(whatsappMessage);
            window.location.href = whatsappURL;
        }
    });
})();

// CTA fijo con tracking
(function(){
  var PATH = location.pathname;
  var wa = document.getElementById("cta-whatsapp");
  var tl = document.getElementById("cta-llamar");

  window.dataLayer = window.dataLayer || [];
  function pushEvt(type, label) {
    try {
      window.dataLayer.push({
        event: "cta_click",
        cta_type: type,
        cta_label: label,
        page: PATH
      });
    } catch(e) {}
  }

  if (wa) {
    wa.addEventListener("click", function() {
      pushEvt("whatsapp", "cta_floating");
    });
  }
  if (tl) {
    tl.addEventListener("click", function() {
      pushEvt("llamar", "cta_floating");
    });
  }
})();

// Mini footer nav tracking
(function(){
  window.dataLayer=window.dataLayer||[];
  document.querySelectorAll(".site-mini-nav a").forEach(function(a){
    if(a.dataset.navBound==="1") return; a.dataset.navBound="1";
    a.addEventListener("click", function(){
      try{ dataLayer.push({event:"nav_click", nav_label:a.textContent.trim(), nav_href:a.getAttribute("href"), page:location.pathname}); }catch(e){}
    });
  });
})();

// Tracking de tarjetas SEO - diferido con requestIdleCallback
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
  document.querySelectorAll('.seo-card[data-event="click_seo_card"]').forEach(function(card) {
    card.addEventListener('click', function(e) {
      var cardName = this.getAttribute('data-card-name');
      var cardPosition = this.getAttribute('data-card-position');
      var cardHref = this.getAttribute('href');

      try {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          'event': 'click_seo_card',
          'card_name': cardName,
          'card_position': cardPosition,
          'card_url': cardHref,
          'page_location': window.location.pathname
        });
      } catch(e) {}
    });
  });

  // Scroll depth tracking
  var scrollDepths = [25, 50, 75, 90];
  var scrollTracked = {};
  var scrollTicking = false;
  var cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;

  window.addEventListener('resize', function() {
    cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
  }, { passive: true });

  window.addEventListener('scroll', function() {
    if (scrollTicking) return;
    scrollTicking = true;
    requestAnimationFrame(function() {
      var scrollPercent = Math.round((window.scrollY / cachedScrollableHeight) * 100);
      for (var i = 0; i < scrollDepths.length; i++) {
        var depth = scrollDepths[i];
        if (scrollPercent >= depth && !scrollTracked[depth]) {
          scrollTracked[depth] = true;
          try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
              'event': 'scroll_depth',
              'scroll_percentage': depth,
              'page_location': window.location.pathname
            });
          } catch(e) {}
        }
      }
      scrollTicking = false;
    });
  }, { passive: true });
})();

// Exit-Intent Popup
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var popup = document.getElementById('exit-intent-popup');
    if (!popup) return;

    var closeBtn = document.querySelector('.exit-popup-close');
    var whatsappBtn = document.getElementById('exit-popup-whatsapp');
    var phoneBtn = document.getElementById('exit-popup-phone');
    var popupShown = false;
    var SESSION_KEY = 'exitPopupShown';

    if (sessionStorage.getItem(SESSION_KEY)) return;

    function isMobile() {
        return window.innerWidth <= 768 || 'ontouchstart' in window;
    }

    function showPopup() {
        if (popupShown) return;
        popupShown = true;
        sessionStorage.setItem(SESSION_KEY, 'true');
        popup.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_shown',
                'page_location': window.location.pathname,
                'trigger': isMobile() ? 'mobile_timer' : 'desktop_mouseleave'
            });
        } catch(e) {}
    }

    function hidePopup() {
        popup.style.display = 'none';
        document.body.style.overflow = '';

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_closed',
                'page_location': window.location.pathname
            });
        } catch(e) {}
    }

    if (!isMobile()) {
        document.addEventListener('mouseleave', function(e) {
            if (e.clientY < 10) showPopup();
        });
    }

    if (isMobile()) {
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function() {
            if (!popupShown) {
                showPopup();
                history.pushState(null, '', location.href);
            }
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            hidePopup();
        });
    }

    popup.addEventListener('click', function(e) {
        if (e.target === popup) {
            hidePopup();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (popup.style.display === 'flex' && e.key === 'Escape') {
            hidePopup();
        }
    });

    if (whatsappBtn) {
        whatsappBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_whatsapp_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }

    if (phoneBtn) {
        phoneBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_phone_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }
}, 2500);

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {})
            .catch(err => {});
    });
}

// Bottom Sheet Cotizacion Movil
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var trigger = document.getElementById('quote-trigger');
    var overlay = document.getElementById('quote-overlay');
    var sheet = document.getElementById('quote-sheet');
    var closeBtn = document.querySelector('.quote-sheet-close');
    var form = document.getElementById('quote-form');
    var chips = document.querySelectorAll('.quote-chip');

    if (!trigger || !sheet) return;

    var selectedService = '';
    var scrollY = 0;

    var focusableElements = sheet.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    var firstFocusable = focusableElements[0];
    var lastFocusable = focusableElements[focusableElements.length - 1];

    function openSheet() {
        scrollY = window.scrollY;
        document.body.classList.add('quote-sheet-open');
        overlay.classList.add('active');
        sheet.classList.add('active');
        sheet.setAttribute('aria-hidden', 'false');
        overlay.setAttribute('aria-hidden', 'false');

        var firstInput = sheet.querySelector('input');
        if (firstInput) {
            setTimeout(function() { firstInput.focus(); }, 100);
        }

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'quote_sheet_open',
                'page_location': window.location.pathname
            });
        } catch(e) {}
    }

    function closeSheet() {
        document.body.classList.remove('quote-sheet-open');
        overlay.classList.remove('active');
        sheet.classList.remove('active');
        sheet.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('aria-hidden', 'true');
        window.scrollTo(0, scrollY);
        trigger.focus();
    }

    trigger.addEventListener('click', openSheet);
    overlay.addEventListener('click', closeSheet);

    if (closeBtn) {
        closeBtn.addEventListener('click', closeSheet);
    }

    var touchStartY = 0;
    var touchCurrentY = 0;
    var handle = sheet.querySelector('.quote-sheet-handle');

    if (handle) {
        handle.addEventListener('touchstart', function(e) {
            touchStartY = e.touches[0].clientY;
        }, { passive: true });

        handle.addEventListener('touchmove', function(e) {
            touchCurrentY = e.touches[0].clientY;
            var deltaY = touchCurrentY - touchStartY;
            if (deltaY > 0) {
                sheet.style.transform = 'translateY(' + deltaY + 'px)';
            }
        }, { passive: true });

        handle.addEventListener('touchend', function() {
            var deltaY = touchCurrentY - touchStartY;
            if (deltaY > 100) {
                closeSheet();
            }
            sheet.style.transform = '';
            touchStartY = 0;
            touchCurrentY = 0;
        });
    }

    document.addEventListener('keydown', function(e) {
        if (!sheet.classList.contains('active')) return;

        if (e.key === 'Escape') {
            closeSheet();
            return;
        }

        if (e.key === 'Tab') {
            if (e.shiftKey) {
                if (document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                }
            } else {
                if (document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        }
    });

    chips.forEach(function(chip) {
        chip.addEventListener('click', function() {
            chips.forEach(function(c) { c.classList.remove('selected'); });
            this.classList.add('selected');
            selectedService = this.getAttribute('data-service');
        });
    });

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var nombre = document.getElementById('quote-nombre').value.trim();
            var whatsapp = document.getElementById('quote-whatsapp').value.trim();
            var mensaje = document.getElementById('quote-mensaje').value.trim();

            if (!nombre || !whatsapp) {
                alert('Por favor completa los campos obligatorios.');
                return;
            }

            var msg = 'Hola! Necesito servicio de llantera a domicilio:\n\n';
            msg += 'Nombre: ' + nombre + '\n';
            msg += 'WhatsApp: ' + whatsapp + '\n';
            if (selectedService) {
                msg += 'Servicio: ' + selectedService + '\n';
            }
            if (mensaje) {
                msg += 'Detalle: ' + mensaje + '\n';
            }

            var whatsappURL = 'https://wa.me/526673922273?text=' + encodeURIComponent(msg);

            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'generate_lead',
                    'form_name': 'quote_sheet_mobile',
                    'method': 'whatsapp',
                    'service': selectedService || 'no_especificado',
                    'value': 1,
                    'currency': 'MXN'
                });
            } catch(e) {}

            try {
                var leads = JSON.parse(localStorage.getItem('llantero_leads') || '[]');
                leads.push({
                    timestamp: new Date().toISOString(),
                    nombre: nombre,
                    whatsapp: whatsapp,
                    servicio: selectedService,
                    mensaje: mensaje,
                    source: 'quote_sheet_mobile',
                    url: window.location.href
                });
                localStorage.setItem('llantero_leads', JSON.stringify(leads));
            } catch(e) {}

            window.open(whatsappURL, '_blank');

            closeSheet();
            form.reset();
            chips.forEach(function(c) { c.classList.remove('selected'); });
            selectedService = '';
        });
    }

    var whatsappInput = document.getElementById('quote-whatsapp');
    if (whatsappInput) {
        whatsappInput.addEventListener('input', function() {
            this.value = this.value.replace(/\D/g, '');
        });
    }
});

// Hide floating buttons in critical sections
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var floatingBtns = document.querySelectorAll('.floating-btn');
    var quoteTrigger = document.getElementById('quote-trigger');
    if (!floatingBtns.length) return;

    var criticalSections = document.querySelectorAll('.hero, #contacto, .footer, .contact-form, .map-embed');
    if (!criticalSections.length) return;

    var isHidden = false;
    var menuOpen = false;
    var sheetOpen = false;

    var bodyObserver = new MutationObserver(function(mutations) {
        menuOpen = document.body.classList.contains('menu-open');
        sheetOpen = document.body.classList.contains('quote-sheet-open');
    });
    bodyObserver.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    function updateVisibility(shouldHide) {
        if (shouldHide === isHidden) return;
        isHidden = shouldHide;
        var opacity = shouldHide ? '0' : '1';
        var pointer = shouldHide ? 'none' : 'auto';
        for (var i = 0; i < floatingBtns.length; i++) {
            floatingBtns[i].style.cssText = 'opacity:' + opacity + ';pointer-events:' + pointer;
        }
        if (quoteTrigger && !sheetOpen) {
            quoteTrigger.style.cssText = 'opacity:' + opacity + ';pointer-events:' + pointer;
        }
    }

    var observer = new IntersectionObserver(function(entries) {
        var anyVisible = false;
        for (var i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting && entries[i].intersectionRatio > 0.3) {
                anyVisible = true;
                break;
            }
        }
        if (!menuOpen) updateVisibility(anyVisible);
    }, {
        threshold: [0, 0.3, 0.5],
        rootMargin: '0px 0px -100px 0px'
    });

    criticalSections.forEach(function(section) {
        observer.observe(section);
    });
});


// ===== TRACKING EVENTS =====

// EVENTO A: Global tracking para enlaces tel: y wa.me
(function() {
      document.addEventListener('click', function(e) {
              var link = e.target.closest('a[href^="tel:"], a[href*="wa.me"]');
              if (!link) return;
              var href = link.getAttribute('href');
              var tipo = href.startsWith('tel:') ? 'phone' : 'whatsapp';
              var numero = href.replace(/[^\d]/g, '');
              try {
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                                    'event': 'contact_link_click',
                                    'contact_type': tipo,
                                    'phone_number': numero,
                                    'page_location': window.location.pathname,
                                    'link_text': link.textContent.trim().substring(0, 50),
                                    'link_location': link.getBoundingClientRect().y > window.innerHeight/2 ? 'below_fold' : 'above_fold'
                        });
              } catch(e) {}
      }, true);
})();

// EVENTO B: Time on Page tracking (30s, 60s, 120s, 300s)
(function() {
      var timeOnPageSegments = [30, 60, 120, 300];
      var timeTracked = {};
      var startTime = Date.now();
      setInterval(function() {
              var currentTime = Math.floor((Date.now() - startTime) / 1000);
              for (var i = 0; i < timeOnPageSegments.length; i++) {
                        var segment = timeOnPageSegments[i];
                        if (currentTime >= segment && !timeTracked[segment]) {
                                    timeTracked[segment] = true;
                                    try {
                                                  window.dataLayer = window.dataLayer || [];
                                                  window.dataLayer.push({
                                                                  'event': 'page_time_milestone',
                                                                  'time_seconds': segment,
                                                                  'page_location': window.location.pathname
                                                  });
                                    } catch(e) {}
                        }
              }
      }, 1000);
})();

// EVENTO C: Internal navigation links tracking
(function() {
      var mainNavLinks = document.querySelectorAll('a[href^="/servicios/"], a[href^="/blog/"], a[href^="/llantero-colonias/"]');
      mainNavLinks.forEach(function(link) {
              link.addEventListener('click', function(e) {
                        var href = this.getAttribute('href');
                        var text = this.textContent.trim().substring(0, 100);
                        var pageType = 'internal_link';
                        if (href.includes('/servicios/')) pageType = 'service_page';
                        if (href.includes('/blog/')) pageType = 'blog_page';
                        if (href.includes('/llantero-colonias/')) pageType = 'colony_page';
                        try {
                                    window.dataLayer = window.dataLayer || [];
                                    window.dataLayer.push({
                                                  'event': 'internal_link_click',
                                                  'link_text': text,
                                                  'link_url': href,
                                                  'page_type': pageType,
                                                  'page_location': window.location.pathname
                                    });
                        } catch(e) {}
              });
      });
})();

// EVENTO D: Page type detection (servicios, blog, colonias)
(function() {
      var pathname = window.location.pathname;
      if (pathname.includes('/servicios/')) {
              var serviceMatch = pathname.match(/servicios\/([^\/]+)/);
              var serviceName = serviceMatch ? serviceMatch[1].replace(/-/g, ' ') : 'unknown';
              try {
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                                    'event': 'view_service_page',
                                    'service_name': serviceName,
                                    'page_location': pathname
                        });
              } catch(e) {}
      }
      if (pathname.includes('/llantero-colonias-culiacan/')) {
              var colonyMatch = pathname.match(/llantero-colonias-culiacan\/([^\/]+)/);
              var colonyName = colonyMatch ? colonyMatch[1].replace(/-/g, ' ') : 'unknown';
              try {
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                                    'event': 'view_colony_page',
                                    'colony_name': colonyName,
                                    'page_location': pathname
                        });
              } catch(e) {}
      }
      if (pathname.includes('/blog/')) {
              var postMatch = pathname.match(/blog\/([^\/]+)/);
              var postTitle = postMatch ? postMatch[1].replace(/-/g, ' ') : 'unknown';
              try {
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                                    'event': 'view_blog_post',
                                    'post_title': postTitle,
                                    'page_location': pathname
                        });
              } catch(e) {}
      }
})();

// ===== FIN DE TRACKING EVENTS =====

// Lazy-load Google Maps iframe (ahorra ~500KB en carga inicial)
(function() {
    var mapContainer = document.getElementById('map-lazy');
    if (!mapContainer) return;

    var mapSrc = mapContainer.getAttribute('data-src');
    if (!mapSrc) return;

    var loaded = false;

    function loadMap() {
        if (loaded) return;
        loaded = true;
        var iframe = document.createElement('iframe');
        iframe.src = mapSrc;
        iframe.allowFullscreen = true;
        iframe.referrerPolicy = 'no-referrer-when-downgrade';
        iframe.title = 'Cobertura Llantero Movil Culiacan Pro';
        iframe.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:100%;border:0';
        mapContainer.innerHTML = '';
        mapContainer.appendChild(iframe);
    }

    // Cargar al hacer click/tap en el placeholder
    mapContainer.addEventListener('click', loadMap);

    // Cargar al hacer scroll cerca del mapa (200px antes de ser visible)
    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            if (entries[0].isIntersecting) {
                loadMap();
                observer.disconnect();
            }
        }, { rootMargin: '200px' });
        observer.observe(mapContainer);
    }
})();
