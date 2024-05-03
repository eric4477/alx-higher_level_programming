$(document).ready(function() {
    const addItem = $('#add_item');
    const ul = $('.my_list');

    addItem.on('click', function() {
        const li = $('<li>').text('Item');
        ul.append(li);
    });
});