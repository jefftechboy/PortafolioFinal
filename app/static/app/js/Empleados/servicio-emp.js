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
    navLinks[0].addEventListener('click', () => window.location.href = '/habitaciones/');
    navLinks[1].addEventListener('click', () => window.location.href = '/cliente-emp/');
    navLinks[2].addEventListener('click', () => window.location.href = '/reserva/'); // ya está activo
    
  }
});



function eliminarServicioConfirmacion(id){
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
          window.location.href="/eliminar_servicio_ext/"+id+"/"
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
