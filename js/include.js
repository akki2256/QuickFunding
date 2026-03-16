(function () {
  var headerPlaceholder = document.getElementById('header-placeholder');
  var footerPlaceholder = document.getElementById('footer-placeholder');

  function injectPartial(placeholder, html) {
    if (!placeholder || !html) return;
    var wrap = document.createElement('div');
    wrap.innerHTML = html.trim();
    var element = wrap.firstElementChild;
    if (element) placeholder.replaceWith(element);
  }

  function loadMainScript() {
    var s = document.createElement('script');
    s.src = 'js/main.js';
    s.async = false;
    document.body.appendChild(s);
  }

  Promise.all([
    headerPlaceholder ? fetch('partials/header.html').then(function (r) { return r.text(); }) : Promise.resolve(''),
    footerPlaceholder ? fetch('partials/footer.html').then(function (r) { return r.text(); }) : Promise.resolve('')
  ]).then(function (results) {
    injectPartial(headerPlaceholder, results[0]);
    injectPartial(footerPlaceholder, results[1]);
    loadMainScript();
  }).catch(function () {
    loadMainScript();
  });
})();
