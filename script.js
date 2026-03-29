/* ============================================================
   ALPHA TOURS — script.js
   ============================================================ */

/* ── Mobile Navigation Toggle ── */
const navToggle = document.querySelector('.nav-toggle');
const navLinks  = document.querySelector('.nav-links');

navToggle?.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

// Close nav when a link is clicked (mobile UX)
navLinks?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

// Close nav when clicking outside
document.addEventListener('click', e => {
  if (navLinks?.classList.contains('open') &&
      !navLinks.contains(e.target) &&
      !navToggle?.contains(e.target)) {
    navLinks.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
});

/* ── Header: hide on scroll down, reveal on scroll up ── */
const header = document.querySelector('.site-header');
let lastScrollY = window.scrollY;
let scrollTicking = false;

window.addEventListener('scroll', () => {
  if (scrollTicking) return;
  scrollTicking = true;
  window.requestAnimationFrame(() => {
    const currentScrollY = window.scrollY;
    const isMenuOpen = navToggle?.getAttribute('aria-expanded') === 'true';

    if (!isMenuOpen) {
      if (currentScrollY > lastScrollY && currentScrollY > 180) {
        header?.classList.add('header-hidden');
      } else {
        header?.classList.remove('header-hidden');
      }
    }

    header?.classList.toggle('scrolled', currentScrollY > 80);
    lastScrollY = currentScrollY;
    scrollTicking = false;
  });
}, { passive: true });

/* ── Active Nav Link Highlighting ── */
const currentFile = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentFile || (currentFile === '' && href === 'index.html')) {
    link.setAttribute('aria-current', 'page');
  }
});

/* ── Scroll-Reveal via IntersectionObserver ── */
// Targets: service cards, tour cards, blog cards, feature vehicle, and any .reveal element
const revealTargets = document.querySelectorAll(
  '.service-card, .tour-card, .blog-card, .feature-visual, .reveal'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const delay = Number(entry.target.dataset.delay ?? 0);
    setTimeout(() => {
      entry.target.classList.add('reveal-done');
    }, delay);
    revealObserver.unobserve(entry.target);
  });
}, {
  threshold: 0.12,
  rootMargin: '0px 0px -40px 0px'
});

// Stagger cards within grids
revealTargets.forEach(el => {
  if (el.classList.contains('service-card') ||
      el.classList.contains('tour-card') ||
      el.classList.contains('blog-card')) {
    const siblings = [...el.parentElement.children].filter(
      c => c.classList.contains(el.classList[0])
    );
    const idx = siblings.indexOf(el);
    el.dataset.delay = idx * 85;
  }
  revealObserver.observe(el);
});

/* ── FAQ: Accordion (close others on open) ── */
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
  item.addEventListener('toggle', () => {
    if (item.open) {
      faqItems.forEach(other => {
        if (other !== item && other.open) other.open = false;
      });
    }
  });
});

/* ── Contact Form ── */
const contactForm    = document.querySelector('.contact-form');
const formSuccess    = document.querySelector('.form-success');
const formWrap       = document.querySelector('.contact-form-wrap');

contactForm?.addEventListener('submit', e => {
  e.preventDefault();
  const submitBtn = contactForm.querySelector('[type="submit"]');
  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending…';

  // Simulate submission — replace with real fetch() to your endpoint
  setTimeout(() => {
    contactForm.style.display = 'none';
    if (formSuccess) {
      formSuccess.style.display = 'block';
      formSuccess.innerHTML = `
        <div style="font-size:2.5rem;margin-bottom:1rem;">✓</div>
        <strong>Message sent!</strong><br>
        <span style="font-weight:400;font-size:0.95rem;opacity:0.85">
          We'll get back to you within 24 hours.
        </span>`;
    }
  }, 900);
});

/* ── Newsletter Form ── */
const newsletterForm = document.querySelector('.newsletter-form');
newsletterForm?.addEventListener('submit', e => {
  e.preventDefault();
  const parent = newsletterForm.parentElement;
  parent.innerHTML = `
    <p style="color:var(--color-primary);font-weight:700;font-size:1.1rem;">
      ✓ You're subscribed! Benvenuto alla famiglia Alpha Tours.
    </p>`;
});

/* ── Smooth anchor scroll for # links ── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const top = target.getBoundingClientRect().top + window.scrollY
              - parseInt(getComputedStyle(document.documentElement)
                  .getPropertyValue('--header-height'), 10) - 16;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

/* ── Scroll-Driven Video ── */
(function () {
  const section     = document.querySelector('.scroll-video-section');
  const video       = document.querySelector('.scroll-video');
  const bar         = document.querySelector('.scroll-video-progress-bar');
  const content     = document.querySelector('.scroll-video-content');
  if (!section || !video) return;

  video.pause();
  video.currentTime = 0;

  // Prime first frame on mobile (iOS/Android ignore preload)
  function primeFirstFrame() {
    video.play().then(() => { video.pause(); video.currentTime = 0; }).catch(() => {});
  }
  if (video.readyState >= 1) {
    primeFirstFrame();
  } else {
    video.addEventListener('loadedmetadata', primeFirstFrame, { once: true });
  }

  let targetProgress  = 0;
  let displayProgress = 0;
  let ticking         = false;

  function getProgress() {
    const rect      = section.getBoundingClientRect();
    const scrollable = section.offsetHeight - window.innerHeight;
    return Math.max(0, Math.min(1, -rect.top / scrollable));
  }

  function tick() {
    // Lerp toward target for buttery smoothness
    displayProgress += (targetProgress - displayProgress) * 0.14;

    if (video.duration && isFinite(video.duration) && video.readyState >= 2) {
      const t = displayProgress * video.duration;
      if (Math.abs(video.currentTime - t) > 0.015) {
        video.currentTime = t;
      }
    }

    if (bar) bar.style.width = (displayProgress * 100) + '%';
    if (content) {
      const inView = displayProgress > 0.06 && displayProgress < 0.94;
      content.classList.toggle('visible', inView);
    }

    if (Math.abs(displayProgress - targetProgress) > 0.001) {
      requestAnimationFrame(tick);
    } else {
      ticking = false;
    }
  }

  window.addEventListener('scroll', () => {
    targetProgress = getProgress();
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(tick);
    }
  }, { passive: true });
}());

/* ── Year in footer ── */
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();
