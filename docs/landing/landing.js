(() => {
  const englishView = document.getElementById('english-view');
  const pictiqView = document.getElementById('pictiq-view');
  const modeButtons = [...document.querySelectorAll('[data-mode]')];
  const nav = document.querySelector('.nav');

  function setMode(mode, { updateUrl = true } = {}) {
    const pictiq = mode === 'pictiq';
    const y = window.scrollY;
    englishView.hidden = pictiq;
    pictiqView.hidden = !pictiq;
    if (nav) nav.hidden = pictiq;
    modeButtons.forEach((button) => {
      const active = button.dataset.mode === (pictiq ? 'pictiq' : 'en');
      button.setAttribute('aria-pressed', String(active));
    });
    document.documentElement.dataset.mode = pictiq ? 'pictiq' : 'en';
    if (updateUrl) {
      const url = new URL(window.location.href);
      if (pictiq) url.searchParams.set('mode', 'pictiq');
      else url.searchParams.delete('mode');
      window.history.replaceState({}, '', url);
    }
    window.requestAnimationFrame(() => window.scrollTo({ top: y, behavior: 'auto' }));
  }

  modeButtons.forEach((button) => button.addEventListener('click', () => setMode(button.dataset.mode)));
  setMode(new URLSearchParams(window.location.search).get('mode') === 'pictiq' ? 'pictiq' : 'en', { updateUrl: false });

  const card = document.querySelector('.book-tilt');
  if (!card || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const reset = () => { card.style.transform = ''; card.style.boxShadow = ''; };
  card.addEventListener('pointermove', (event) => {
    if (event.pointerType === 'touch') return;
    const rect = card.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width - 0.5;
    const y = (event.clientY - rect.top) / rect.height - 0.5;
    const rotateX = (-y * 4).toFixed(2);
    const rotateY = (x * 4).toFixed(2);
    card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-2px)`;
    card.style.boxShadow = `${(-x * 10).toFixed(0)}px ${(8 - y * 10).toFixed(0)}px 28px rgba(0,0,0,0.14)`;
  });
  card.addEventListener('pointerleave', reset);
  card.addEventListener('blur', reset);
})();
