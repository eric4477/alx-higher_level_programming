$(document).ready(function() {
    const header = $('header');
    const redHeader = $('#red_header');

    redHeader.on('click', function() {
        header.addClass("red")
    })
})