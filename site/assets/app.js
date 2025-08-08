document.addEventListener('DOMContentLoaded', function () {
  const dropdownButtons = document.querySelectorAll('.lh-group .lh-nav-btn');
  dropdownButtons.forEach((button) => {
    const group = button.closest('.lh-group');
    button.addEventListener('mouseenter', function () {
      const icon = this.querySelector('i');
      if (!icon) return;
      icon.classList.remove('ri-arrow-down-s-line');
      icon.classList.add('ri-arrow-up-s-line');
    });
    group.addEventListener('mouseleave', function () {
      const icon = this.querySelector('i');
      if (!icon) return;
      icon.classList.remove('ri-arrow-up-s-line');
      icon.classList.add('ri-arrow-down-s-line');
    });
  });

  const ctaButton = document.querySelector('.lh-cta');
  if (ctaButton) {
    ctaButton.addEventListener('click', function () {
      this.style.transform = 'scale(0.95)';
      setTimeout(() => { this.style.transform = 'scale(1.05)'; }, 100);
      setTimeout(() => { this.style.transform = 'scale(1)'; }, 200);
    });
  }
});