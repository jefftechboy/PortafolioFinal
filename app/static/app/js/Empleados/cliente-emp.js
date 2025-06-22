document.addEventListener('DOMContentLoaded', function () {
  const logoImg = document.querySelector('.logo');
  if (logoImg) {
    logoImg.style.cursor = 'pointer';
    logoImg.addEventListener('click', function () {
      window.location.href = '/inicio.html/';
    });
  }
});
document.addEventListener('DOMContentLoaded', function () {
  // Redirigir al login desde el ícono de perfil
  const perfilIcon = document.querySelector('.perfil-icon');
  if (perfilIcon) {
    perfilIcon.addEventListener('click', function () {
      window.location.href = '/login/';
    });
  }

  // Enlaces del navbar
  
const navLinks = document.querySelectorAll('nav a');
  if (navLinks.length) {
    navLinks[0].addEventListener('click', () => window.location.href = '/servicios/');
    navLinks[1].addEventListener('click', () => window.location.href = '/habitaciones/');
    navLinks[2].addEventListener('click', () => window.location.href = '/cliente-emp/');
    navLinks[3].addEventListener('click', () => window.location.href = '/reserva/'); // ya está activo
    navLinks[4].addEventListener('click', () => window.location.href = '/agenda/');
  }
});