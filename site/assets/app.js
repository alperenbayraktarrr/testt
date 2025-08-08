document.addEventListener('DOMContentLoaded', function () {
  const dropdownButtons = document.querySelectorAll('.group button');
  dropdownButtons.forEach((button) => {
    const group = button.closest('.group');
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

  const exploreButton = document.querySelector('main button');
  const clientLogos = document.querySelectorAll('.w-16.h-16');
  if (exploreButton) {
    exploreButton.addEventListener('click', function () {
      this.style.transform = 'scale(0.95)';
      setTimeout(() => {
        this.style.transform = 'scale(1.05)';
      }, 100);
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 200);
    });
  }
  clientLogos.forEach((logo) => {
    logo.addEventListener('mouseenter', function () {
      this.style.transform = 'scale(1.1)';
    });
    logo.addEventListener('mouseleave', function () {
      this.style.transform = 'scale(1)';
    });
  });
});