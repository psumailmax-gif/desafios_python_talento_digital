$(document).ready(function() {
    
    // 1. Inicialización de los Tooltips de Bootstrap 5
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // 2. Alerta al hacer clic en "Enviar por correo" (ID #enviarCorreo)
    $('#enviarCorreo').on('click', function() {
        alert("El correo fue enviado correctamente...");
    });

    // 3. Cambiar el color del texto a rojo al hacer doble clic en los títulos (INGREDIENTES y PREPARACIÓN)
    $('.section_ingre_prepa h4').on('dblclick', function() {
        $(this).toggleClass('text-danger-custom');
    });

    // 4. Mostrar u ocultar el contenido de las tarjetas de recetas al hacer clic en sus títulos
    $('.seccion_recetas .card-title').on('click', function() {
        $(this).siblings('.card-text').toggle(400);
    });

});