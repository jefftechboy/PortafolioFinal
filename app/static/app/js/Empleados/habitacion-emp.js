document.addEventListener('DOMContentLoaded', function () {
const modificarLinks = document.querySelectorAll('.btn-warning');
const crearBtn = document.querySelector('.crear-btn');

modificarLinks.forEach(link => {
    link.addEventListener('click', function (event) {
    // Evita que el enlace redireccione de inmediato
    event.preventDefault();

    // Desactiva el botón "Crear Nuevo"
    crearBtn.textContent = 'Modo Edición';
    crearBtn.classList.add('disabled'); // Añade clase para estilos si quieres
    crearBtn.setAttribute('disabled', true); // Desactiva botón si es <button>
    crearBtn.style.pointerEvents = 'none'; // Inhabilita clics

    // Redirige después de un breve retraso para permitir los cambios visuales
    setTimeout(() => {
        window.location.href = link.href;
    }, 100); // tiempo en milisegundos
    });
});
});
