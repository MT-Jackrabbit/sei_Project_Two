console.log('app.js loaded correctly');

$(document).ready(() => {
    const errLogin = $('#login-errors').text();
    const errSignup = $('#signup-errors').text();

    if(errLogin === 'Errors:')
        $('#logInModal').modal('show');
    else if(errSignup === 'Errors:')
        $('#signUpModal').modal('show');

    $('#content').attr('maxlength', '3000');

});

$('#span__username').click(() => {
    //alert($('#div__help-username').text());
    $('#div__help-username').toggle();
});

$('#span__password1').click(() => {
    // alert($('#div__help-password1').text());
    $('#div__help-password1').toggle();
});

$('#span__password2').click(() => {
    // alert($('#div__help-password2').text());
    $('#div__help-password2').toggle();
});

$('#id_name').blur(() => {
    const name = $('#id_name').val();
    $('#id_name').val($.trim(name));
});

$('#id_username').blur(() => {
    const username = $('#id_username').val();
    $('#id_username').val($.trim(username));
});

$('#a__login').mouseenter(() => {
    $('#login-txt').css('opacity', '1');
});

$('#a__login').mouseleave(() => {
    $('#login-txt').css('opacity', '0');
});

$('#a__signup').mouseenter(() => {
    $('#signup-txt').css('opacity', '1');
});

$('#a__signup').mouseleave(() => {
    $('#signup-txt').css('opacity', '0');
});

$('#a__logout').mouseenter(() => {
    $('#logout-txt').css('opacity', '1');
});

$('#a__logout').mouseleave(() => {
    $('#logout-txt').css('opacity', '0');
});

$('#a__profile').mouseenter(() => {
    $('#profile-txt').css('opacity', '1');
});

$('#a__profile').mouseleave(() => {
    $('#profile-txt').css('opacity', '0');
});