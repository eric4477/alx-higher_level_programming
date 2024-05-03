$(document).ready(function() {
    const header = $('header');
    const toggleHeader = $('#toggle_header');

    toggleHeader.on('click', function() {
        header.toggleClass("green red");
    });
});