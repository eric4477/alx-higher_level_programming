$(document).ready(function() {
    const ul = $('#list_movies');

    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            data.results.forEach(function(result) {
                const li = $('<li>').text(result.title);
                ul.append(li);
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('There was a problem with the fetch operation:', errorThrown);
        }
    });
});
