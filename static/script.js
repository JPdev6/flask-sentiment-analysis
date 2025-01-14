// Enable Bootstrap validation
(function () {
    'use strict';

    // Fetch all forms
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over forms and prevent submission if invalid
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})();
