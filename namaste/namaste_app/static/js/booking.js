$(document).ready(function(){
    $('.btn-default').click(function(){
        // Find the h3 text related to the clicked button using the class
        var packageTitle = $(this).closest('.package').find('.package-title').text();

        // Check if the packageTitle is 'Maquina de Gluteos'
        if(packageTitle === 'Maquina de Gluteos') {
            packageTitle = 'Vacumterapia'; // Change the value to 'Vacumterapia'
        }

        // Set the text in the modal's input field
        $('#selected-package').val(packageTitle);
    });
});

