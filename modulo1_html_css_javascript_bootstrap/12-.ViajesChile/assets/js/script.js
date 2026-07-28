$(document).ready(function () {
    // 1. Inicialización de Tooltips de Bootstrap
    $('[data-toggle="tooltip"]').tooltip();

    // 2. Smooth Scroll para enlaces del Navbar
    $("a.nav-link").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top - 55
            }, 800);
        }
    });

    // 3. Evento para alertar el envío de formulario
    $('#form-contacto').on('submit', function (e) {
        e.preventDefault();
        alert('¡Gracias por comunicarte con Viajes Chile! Tu mensaje ha sido enviado exitosamente.');
        this.reset();
    });
});