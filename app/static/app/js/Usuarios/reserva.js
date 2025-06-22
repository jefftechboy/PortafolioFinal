function calcularTotal() {
    const inicio = new Date(document.getElementById("fechaInicio").value);
    const fin = new Date(document.getElementById("fechaFin").value);
    let dias = Math.ceil((fin - inicio) / (1000 * 60 * 60 * 24));
    if (dias < 0 || isNaN(dias)) dias = 0;
  
    const habitacionRaw = document.getElementById("habitacion").value;
    const servicio = parseInt(document.getElementById("servicio").value);
    const extra = parseInt(document.getElementById("extra").value);
  
    let total = 0;
    let cantidadPersonas = 0;
  
    if (habitacionRaw !== "0|0" && dias > 0) {
      const [valorHabitacion, personas] = habitacionRaw.split("|").map(Number);
      total += valorHabitacion * dias;
      cantidadPersonas = personas;
    }
  
    if (servicio > 0) total += servicio;
    if (extra > 0) total += extra;
  
    document.getElementById("total").innerText = `$${total.toLocaleString()}`;
    document.getElementById("infoDias").innerText = `${dias} día${dias === 1 ? '' : 's'}`;
    document.getElementById("infoPersonas").innerText = `${cantidadPersonas} persona${cantidadPersonas === 1 ? '' : 's'}`;
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("fechaInicio").addEventListener("change", calcularTotal);
    document.getElementById("fechaFin").addEventListener("change", calcularTotal);
    document.getElementById("habitacion").addEventListener("change", calcularTotal);
    document.getElementById("servicio").addEventListener("change", calcularTotal);
    document.getElementById("extra").addEventListener("change", calcularTotal);
  });
  