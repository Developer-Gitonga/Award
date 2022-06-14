let hamburger = document.querySelector('.hamburger');
let menu = $('.header-nav-menu')
menu.slideUp()

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    menu.slideToggle();
});
