console.log('The app.js loaded correctly');

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