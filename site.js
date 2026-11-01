(() => {
  const menu = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  if (menu && mobileNav) {
    menu.addEventListener('click', () => {
      const isOpen = menu.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('aria-expanded', String(!isOpen));
      mobileNav.hidden = isOpen;
    });
    mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      menu.setAttribute('aria-expanded', 'false');
      mobileNav.hidden = true;
    }));
    window.addEventListener('resize', () => {
      if (window.innerWidth > 760) {
        mobileNav.hidden = true;
        menu.setAttribute('aria-expanded', 'false');
      }
    });
  }

  const filters = document.querySelectorAll('.filter');
  const items = document.querySelectorAll('.gallery-item');
  filters.forEach(button => button.addEventListener('click', () => {
    filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    const filter = button.dataset.filter;
    items.forEach(item => { item.hidden = filter !== 'all' && !item.dataset.category.split(' ').includes(filter); });
  }));

  const dialog = document.querySelector('.lightbox');
  if (dialog) {
    let lastTrigger;
    items.forEach(item => item.addEventListener('click', () => {
      lastTrigger = item;
      const image = item.querySelector('img');
      const full = dialog.querySelector('img');
      full.src = image.src;
      full.alt = image.alt;
      dialog.querySelector('.lightbox-head p').textContent = image.alt;
      dialog.showModal();
    }));
    dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
    dialog.addEventListener('close', () => lastTrigger?.focus());
  }

  const form = document.querySelector('#contact-form');
  if (form) form.addEventListener('submit', event => {
    event.preventDefault();
    form.querySelector('.demo-result').classList.add('show');
    form.querySelector('.demo-result').focus();
  });
})();
