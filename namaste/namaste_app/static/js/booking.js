$(document).ready(function(){
    $('.btn-default').click(function(){
        // Find the h3 text related to the clicked button using the class
        var packageTitle = $(this).closest('.package').find('.package-title').text();

        // Set the text in the modal's input field
        $('#selected-package').val(packageTitle);
    });
});
