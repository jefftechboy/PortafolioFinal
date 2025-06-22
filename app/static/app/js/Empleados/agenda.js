document.addEventListener("DOMContentLoaded", function () {
      flatpickr("#date", {
        inline: true,
        locale: flatpickr.l10ns.es,
        dateFormat: "d/m/Y",
        defaultDate: "today",
        weekNumbers: true
    });
});