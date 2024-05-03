$(document).ready(function() {
    const divEl = $('#hello');

    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            divEl.text(data.hello); // Set the text content to the value from the API response
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('There was a problem with the fetch operation:', errorThrown);
        }
    });
});
