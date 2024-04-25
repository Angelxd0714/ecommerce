
$(document).ready(function () {
    // Carga el archivo JSON
    fetch("assets/json/lenguage.json")
        .then(response => response.json()) // Parsea el JSON
        .then(languageData => {
            // Inicializa el DataTable con el idioma cargado
            $("#example").DataTable({
                "scrollY": "200px",
                "scrollCollapse": true,
                language: languageData // Utiliza los datos del idioma cargados
            });
        })
        .catch(error => {
            console.error('Error al cargar el archivo JSON:', error);
        });
});