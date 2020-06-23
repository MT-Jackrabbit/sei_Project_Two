// Show more/Show less link for show post 
let POST_TEXT = '';
let MIN_TEXT = '';
const MIN_CHR = 1000;

$(document).ready(function() {
    POST_TEXT = $('.card-text').text();
    if(POST_TEXT.length > MIN_CHR) 
    {
        MIN_TEXT = POST_TEXT.substr(0, MIN_CHR) + '...';
        $('.card-text').text(MIN_TEXT);
    }
    else {
        $('#more_text').hide();
    }
})

$('#more_text').click(() => {
    if($('#more_text').text() === 'Show more')
    {
        $('.card-text').text(POST_TEXT);
        $('#more_text').text('Show less');
    }
    else if($('#more_text').text() === 'Show less')
    {
        $('.card-text').text(MIN_TEXT);
        $('#more_text').text('Show more');
    }
})