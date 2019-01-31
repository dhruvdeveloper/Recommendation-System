$(function() {

    var array = [];
    var array2 = [];
    var a = '';

    $.ajax({
        url: 'http://127.0.0.1:8000/bookjson',
        complete: function(json) {
            data = JSON.parse(json.responseText);
            var i;
            for (i = 0; i < 1000; i++){
                array.push(data[i][1] + '-' + data[i][0]);
            }


            $("#tags2").autocomplete({
                source: function(request, response) {
                    var results = $.ui.autocomplete.filter(array, request.term);
                    response(results.slice(0, 7));
                }
            });
        }
    });
});
