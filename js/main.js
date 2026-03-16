(function () {
  'use strict';

  var navItems = document.querySelectorAll('.nav-item.has-dropdown');

  function closeAllDropdowns() {
    navItems.forEach(function (item) {
      item.classList.remove('is-open');
      var btn = item.querySelector('.nav-link');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }

  navItems.forEach(function (item) {
    var btn = item.querySelector('.nav-link');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var isOpen = item.classList.contains('is-open');
      closeAllDropdowns();
      if (!isOpen) {
        item.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  document.body.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item.has-dropdown')) closeAllDropdowns();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAllDropdowns();
  });

  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
