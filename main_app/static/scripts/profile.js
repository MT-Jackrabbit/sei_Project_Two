console.log("Yea it is working, just changed it.");
$(document).ready(() => {
    // var height = $('.section__post-titles').height()
    // $('.sidebar').height(height)​
    
    $('#update-form').hide();
});

$('#btn__show-update').click(() => {
    $('#update-form').show();
    $('#btn__show-update').toggle();
});

$('#btn__cancel-update').click(() => {
    $('#update-form').hide();
    $('#btn__show-update').toggle();
});