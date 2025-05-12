document.addEventListener("DOMContentLoaded", function() {
    const dropdownBtn = document.querySelector('.dropdown-btn');
    const dropdown = document.querySelector('.dropdown');
  
    dropdownBtn.addEventListener('click', function() {
      dropdown.classList.toggle('open');
    });
  
    // El código para actualizar las opciones seleccionadas permanece igual
    const checkboxes = document.querySelectorAll('.dropdown-content input[type="checkbox"]');
    const selectedOptionsDiv = document.getElementById('selected-options');
  
    function updateSelectedOptions() {
      const selectedOptions = [];
      checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
          selectedOptions.push(checkbox.value);
        }
      });
  
      selectedOptionsDiv.innerHTML = 'Opciones seleccionadas: ' + selectedOptions.join(', ');
    }
  
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', updateSelectedOptions);
    });
  });
  