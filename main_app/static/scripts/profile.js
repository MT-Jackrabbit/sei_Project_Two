console.log("profile.js loaded");

$('#btn__show-update').click(() => {
    $('#update-form').show();
    $('#btn__show-update').toggle();
});

$('#btn__cancel-update').click(() => {
    $('#update-form').hide();
    $('#btn__show-update').toggle();
});