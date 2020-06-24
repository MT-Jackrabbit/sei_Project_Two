console.log('The app.js loaded correctly');

$(document).ready(() => {
    const errLogin = $('#login-errors').text();
    const errSignup = $('#signup-errors').text();

    if(errLogin === 'Errors:')
        $('#logInModal').modal('show');
    else if(errSignup === 'Errors:')
        $('#signUpModal').modal('show');

    $('#content').attr('maxlength', '3000');

});

$('#content').blur(() => {
    const text = $('#content').val();
    alert(text.length);
})

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