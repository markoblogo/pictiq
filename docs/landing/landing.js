(() => {
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
