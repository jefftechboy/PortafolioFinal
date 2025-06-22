document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll('.dropdown-content input[type="checkbox"]');
    const optionsList = document.getElementById('options-list');

    function updateSelectedOptions() {
        // Limpiar lista antes de actualizar
        optionsList.innerHTML = '';

        // Agregar cada opción como una fila <li>
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                const li = document.createElement('li');
                li.textContent = checkbox.value;
                optionsList.appendChild(li);
            }
        });
    }

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateSelectedOptions);
    });
});
