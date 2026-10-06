const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#nav');
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  nav.classList.toggle('open', open);
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', 'Abrir menú');
}));
document.querySelector('#year').textContent = new Date().getFullYear();
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
  }), { threshold: .12 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
} else document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));

const artModal = document.getElementById('artModal');
artModal.addEventListener('show.bs.modal', event => {
 const key = event.relatedTarget.dataset.art;
 const preview = document.getElementById('artPreview');
 let source, title;
 if (key === 'current-scene') {
  const active = document.querySelector('#storyCarousel .carousel-item.active');
  source = active.querySelector('img').getAttribute('src');
  title = active.querySelector('h3').textContent;
 } else {
  const card = document.querySelectorAll('.gallery-item')[Number(key)-1];
  source = card.querySelector('img').getAttribute('src');
  title = card.querySelector('h3').textContent;
 }
 preview.src = source; preview.alt = title;
 document.getElementById('artModalTitle').textContent = title;
});
const pauseStory = document.getElementById('pauseStory');
pauseStory.addEventListener('click', () => {
 const carousel = bootstrap.Carousel.getOrCreateInstance(document.getElementById('storyCarousel'));
 const paused = pauseStory.getAttribute('aria-pressed') !== 'true';
 paused ? carousel.pause() : carousel.cycle();
 pauseStory.setAttribute('aria-pressed', String(paused));
 pauseStory.textContent = paused ? 'Reanudar escenas ▶' : 'Pausar escenas Ⅱ';
});
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
 bootstrap.Carousel.getOrCreateInstance(document.getElementById('storyCarousel')).pause();
 pauseStory.setAttribute('aria-pressed','true');pauseStory.textContent = 'Reanudar escenas ▶';
}
document.getElementById('storyCarousel').addEventListener('slid.bs.carousel', () => {
 if (pauseStory.getAttribute('aria-pressed') === 'true') {
  bootstrap.Carousel.getOrCreateInstance(document.getElementById('storyCarousel')).pause();
 }
});

if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
 bootstrap.Carousel.getOrCreateInstance(document.getElementById('storyCarousel')).cycle();
}
