$(document).ready(function() {
    const header = $('header');
    const updateHeader = $('#update_header');

    updateHeader.on('click', function() {
        header.text("New Header!!!");
    });
});