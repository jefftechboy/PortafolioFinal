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
    navLinks[0].addEventListener('click', () => window.location.href = '/agenda/');
    navLinks[1].addEventListener('click', () => window.location.href = '/servicios/');
    navLinks[2].addEventListener('click', () => window.location.href = '/habitaciones/');
    navLinks[3].addEventListener('click', () => window.location.href = '/reserva/'); // ya está activo
    navLinks[4].addEventListener('click', () => window.location.href = '/agenda/');
  }
});

function imprimirInforme(id) {
  const modal = document.getElementById('modal' + id);
  if (!modal) return;

  const contenido = modal.querySelector('.modal-body').innerHTML;

  const ventana = window.open('', '_blank');
  ventana.document.write(`
    <html>
      <head>
        <title>Informe de Reserva</title>
        <style>
          body { font-family: Arial, sans-serif; padding: 20px; }
          h2 { color: #333; }
          p { margin: 5px 0; }
        </style>
      </head>
      <body>
        <h1>Informe de Reserva N° ${id}</h1>
        ${contenido}
      </body>
    </html>
  `);
  ventana.document.close();
  ventana.focus();
  ventana.print();
}

// Función para descargar PDF usando jsPDF
function descargarInforme(id) {
  const modal = document.getElementById('modal' + id);
  if (!modal) return;

  const contenidoTexto = modal.querySelector('.modal-body').innerText;

  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();

  doc.setFontSize(16);
  doc.text(`Informe de Reserva N° ${id}`, 10, 20);

  doc.setFontSize(12);
  doc.text(contenidoTexto, 10, 30, { maxWidth: 180 });

  doc.save(`informe_reserva_${id}.pdf`);
}
