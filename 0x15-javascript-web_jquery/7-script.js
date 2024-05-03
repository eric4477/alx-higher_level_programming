$(document).ready(function() {
    const header = $('header');

    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            const name = data.name;
            header.text(name);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('There was a problem with the fetch operation:', errorThrown);
        }
    });
});