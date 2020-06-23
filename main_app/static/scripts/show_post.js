console.log("show post js loaded")

$('#btn__show-more').click(() => {

    const text = $('#btn__show-more').text();
    // alert(text)

    if( text === "Show More")
    {
        $('.card-text').css('max-width', '300ch');
        $('#btn__show-more').text("Show Less");
    }
    else if(text === "Show Less")
    {
        $('.card-text').css('max-width', '25ch');
        $('#btn__show-more').text("Show More");
    }

});