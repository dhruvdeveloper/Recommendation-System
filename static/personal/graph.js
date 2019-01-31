$(function() {

    var array = [];
    var array2 = [];
    var a = '';

    $.ajax({
        url: 'http://127.0.0.1:8000/pqrst',
        complete: function(json) {
            data = JSON.parse(json.responseText);
            var i;
            for (i = 0; i < 4000; i++){
                array.push(data[i].title);
            }

            $("#tags").autocomplete({
                source: function(request, response) {
                    var results = $.ui.autocomplete.filter(array, request.term);
                    response(results.slice(0, 7));
                }
            });
        }
    });
});
