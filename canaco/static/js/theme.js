(function () {
  'use strict';

  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nav = document.querySelector('.site-nav');
  var backToTop = document.querySelector('.back-to-top');
  var readingBar = document.querySelector('.reading-progress__bar');

  function onScroll() {
    if (nav) {
      nav.classList.toggle('is-scrolled', window.scrollY > 12);
    }

    if (backToTop) {
      backToTop.classList.toggle('is-visible', window.scrollY > 520);
    }

    if (readingBar) {
      updateReadingProgress();
    }
  }

  function updateReadingProgress() {
    var article = document.querySelector('.post-content-body');
    if (!article || !readingBar) {
      return;
    }

    var rect = article.getBoundingClientRect();
    var viewport = window.innerHeight;
    var total = rect.height + viewport * 0.55;
    var consumed = viewport * 0.55 - rect.top;
    var percent = total > 0 ? (consumed / total) * 100 : 0;

    readingBar.style.width = Math.max(0, Math.min(100, percent)) + '%';
  }

  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
    });
  }

  document.addEventListener(
    'click',
    function (event) {
      var link = event.target.closest('.site-mobile-menu-body a');
      if (link) {
        document.body.classList.remove('offcanvas-menu');
      }
    },
    true
  );

  var revealItems = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));

  if (revealItems.length) {
    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      revealItems.forEach(function (item) {
        item.classList.add('is-visible');
      });
    } else {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              observer.unobserve(entry.target);
            }
          });
        },
        { rootMargin: '0px 0px -40px 0px', threshold: 0.08 }
      );

      revealItems.forEach(function (item) {
        observer.observe(item);
      });
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
})();
