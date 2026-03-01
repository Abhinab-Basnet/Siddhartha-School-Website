/* =============================================
   INDEX PAGE — SIDDHARTHA SECONDARY SCHOOL
   File: core/static/core/js/index.js
   ============================================= */

document.addEventListener('DOMContentLoaded', function () {

    /* ── SCROLL REVEAL ─────────────────────────── */
    const revealEls = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    revealEls.forEach(el => revealObserver.observe(el));


    /* ── NEWS TICKER ───────────────────────────── */
    // Duplicate ticker content so it loops seamlessly
    const tickerContent = document.getElementById('tickerContent');
    if (tickerContent) {
        tickerContent.innerHTML += tickerContent.innerHTML;
    }


    /* ── COUNTER ANIMATION (stats numbers) ─────── */
    const statNumbers = document.querySelectorAll('.stat-number[data-target]');

    const counterObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el     = entry.target;
            const target = parseInt(el.dataset.target, 10);
            const suffix = el.dataset.suffix || '';
            const duration = 1800;
            const step   = Math.ceil(target / (duration / 16));
            let current  = 0;

            const tick = () => {
                current = Math.min(current + step, target);
                el.textContent = current + suffix;
                if (current < target) requestAnimationFrame(tick);
            };

            requestAnimationFrame(tick);
            counterObserver.unobserve(el);
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(el => counterObserver.observe(el));


    /* ── GALLERY LIGHTBOX ──────────────────────── */
    const galleryItems = document.querySelectorAll('.gallery-item img');

    if (galleryItems.length) {
        // Build overlay DOM once
        const overlay = document.createElement('div');
        overlay.id = 'gallery-overlay';
        overlay.innerHTML = `
            <div class="glo-backdrop"></div>
            <div class="glo-content">
                <button class="glo-close" aria-label="Close">&times;</button>
                <button class="glo-prev" aria-label="Previous">&#8249;</button>
                <img class="glo-img" src="" alt="">
                <button class="glo-next" aria-label="Next">&#8250;</button>
                <div class="glo-caption"></div>
            </div>
        `;
        document.body.appendChild(overlay);

        // Minimal inline styles for lightbox (so no extra CSS file needed)
        const style = document.createElement('style');
        style.textContent = `
            #gallery-overlay { position:fixed; inset:0; z-index:9999; display:none; align-items:center; justify-content:center; }
            #gallery-overlay.active { display:flex; }
            .glo-backdrop { position:absolute; inset:0; background:rgba(10,22,40,0.92); backdrop-filter:blur(6px); cursor:pointer; }
            .glo-content  { position:relative; z-index:1; max-width:90vw; max-height:90vh; display:flex; align-items:center; gap:16px; }
            .glo-img      { max-width:80vw; max-height:80vh; border-radius:12px; object-fit:contain; box-shadow:0 20px 60px rgba(0,0,0,0.5); }
            .glo-close    { position:absolute; top:-44px; right:0; background:none; border:none; color:#fff; font-size:2rem; cursor:pointer; line-height:1; }
            .glo-prev, .glo-next { background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); color:#fff; border-radius:50%; width:44px; height:44px; font-size:1.4rem; cursor:pointer; display:flex; align-items:center; justify-content:center; flex-shrink:0; transition:background 0.2s; }
            .glo-prev:hover, .glo-next:hover { background:rgba(201,168,76,0.5); }
            .glo-caption  { position:absolute; bottom:-32px; left:0; right:0; text-align:center; color:rgba(255,255,255,0.5); font-size:0.8rem; }
        `;
        document.head.appendChild(style);

        const imgs     = Array.from(galleryItems);
        let current    = 0;
        const gloImg   = overlay.querySelector('.glo-img');
        const gloCaption = overlay.querySelector('.glo-caption');

        function openAt(idx) {
            current = (idx + imgs.length) % imgs.length;
            gloImg.src = imgs[current].src;
            gloCaption.textContent = imgs[current].alt;
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeOverlay() {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        imgs.forEach((img, i) => img.addEventListener('click', () => openAt(i)));

        overlay.querySelector('.glo-close').addEventListener('click', closeOverlay);
        overlay.querySelector('.glo-backdrop').addEventListener('click', closeOverlay);
        overlay.querySelector('.glo-prev').addEventListener('click', () => openAt(current - 1));
        overlay.querySelector('.glo-next').addEventListener('click', () => openAt(current + 1));

        document.addEventListener('keydown', e => {
            if (!overlay.classList.contains('active')) return;
            if (e.key === 'Escape')     closeOverlay();
            if (e.key === 'ArrowLeft')  openAt(current - 1);
            if (e.key === 'ArrowRight') openAt(current + 1);
        });
    }


    /* ── ACTIVE NAV LINK ───────────────────────── */
    const navLinks = document.querySelectorAll('.nav-links .nav-link');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.color = 'var(--gold-lt)';
        }
    });

});