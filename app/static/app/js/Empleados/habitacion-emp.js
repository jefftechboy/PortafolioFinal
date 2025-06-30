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
function eliminarHabitacionConfirmacion(id){
      const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: "btn btn-success",
          cancelButton: "btn btn-danger"
        },
        buttonsStyling: false
      });
      swalWithBootstrapButtons.fire({
        title: "Confirmar eliminacion",
        text: "La eliminacion sera permanente",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar",
        cancelButtonText: "No, cancelar!",
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href="/eliminar_habitacion_emp/"+id+"/"
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire({
            title: "Cancelado",
            text: "Eliminacion cancelada",
            icon: "error"
          });
        }
      });
    }