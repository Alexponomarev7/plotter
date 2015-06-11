$(document).ready(function() {
    
    var rm_func = function() {
        var tr = $(this).parent().parent();
        var table = tr.parent();
        if(table.children().length > 1){
            tr.remove();
        };

        var arr = table.find("input");
        for(var i = 0; i < arr.length; i++) {
            $(arr[i]).prop("name", "formula" + i);
        }
    };
    
    var add_func = function() {
	var table = $("#texts");
        var tr = $('<tr><td><input name="formula' + table.find("tr").length  + '" type="text"></td><td><button type="button" class="rm_button">Remove</button></td></tr>');
        tr.find("button").click(rm_func);
        table.append(tr);
    }

    $(".rm_button").click(rm_func);

    $("#add").click(add_func);

    $("#bezier").click(function() {
        var table = $("#texts");
        while(table.find("tr").length < 2) {
            add_func();
        }
    });
});
