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


});