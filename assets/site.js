(function () {
  // Theme toggle. The initial data-theme is set by the inline script in <head>.
  var btn = document.getElementById('theme-toggle');
  if (btn) btn.addEventListener('click', function () {
    var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  // Star counts from data/stars.json (refreshed weekly by a GitHub Action).
  // Missing file: the hardcoded fallback text in the page stays as is.
  if (document.querySelector('[data-repo], #total-stars')) {
    fetch('data/stars.json').then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d) return;
      document.querySelectorAll('[data-repo]').forEach(function (el) {
        var n = d[el.getAttribute('data-repo')];
        var s = el.querySelector('.stars');
        if (s && typeof n === 'number') s.textContent = '★ ' + n;
      });
      var t = document.getElementById('total-stars');
      if (t && typeof d._total === 'number') t.textContent = '★ ' + d._total;
    }).catch(function () {});
  }

  // YouTube: thumbnail link first, iframe only after a click. Without JS the link opens YouTube.
  document.querySelectorAll('.yt[data-id]').forEach(function (b) {
    var id = b.getAttribute('data-id');
    b.style.backgroundImage = 'url(https://i.ytimg.com/vi/' + id + '/hqdefault.jpg)';
    b.addEventListener('click', function (ev) {
      ev.preventDefault();
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      f.title = b.getAttribute('aria-label') || 'YouTube video';
      var wrap = document.createElement('div');
      wrap.className = 'yt playing';
      wrap.appendChild(f);
      b.replaceWith(wrap);
    }, { once: true });
  });
})();
