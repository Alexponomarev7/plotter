$(document).ready(function() {
    
    $("#graph").click(function() {
        $(".input").hide();
        $("#functions").show();
        $("#graph_settings").show();
         
        update_functions();
        
        $("#add_btn").show().text("Add function").off("click").click(add_function);
        $("#send_btn").show();
    });
    
    $("#bezier").click(function() {
        $(".input").hide();
        $("#points").show();
        
        update_points();
        
        $("#add_btn").show().text("Add point").off("click").click(add_point);
        $("#send_btn").show();
    });
    
    var rm_element = function() {
        var tr = $(this).parent().parent();
        tr.remove();
        update_functions();
        update_points();
    };
    
    var update_functions = function() {
        while($("#functions").find("tr").length < 1) {
            add_function(true);
        }
        $("#functions").find("tr").each(function(index) {
            $(this).find("p").html("f<sub>" + index + "</sub>(x): ");
            $(this).find(":text").attr("name", "function_" + index);
        });
    };
    
    var update_points = function() {
        while($("#points").find("tr").length < 2) {
            add_point(true);
        }
        $("#points").find("tr").each(function(index) {
            $(this).find("p.x").html("X<sub>" + index + "</sub>: ");
            $(this).find("p.y").html("Y<sub>" + index + "</sub>: ");
            $(this).find(".x:text").attr("name", "x_" + index);
            $(this).find(".y:text").attr("name", "y_" + index);
        });
    };
    
    var add_function = function(not_update) {
        $("#functions").append('<tr><td><p></p></td><td>' +
        '<input type="text" /></td>' + 
        '<td><button type="button" class="rm_btn">Remove</button></td></tr>');
        
        if(not_update != true) {
            update_functions();
        }
        
        $(".rm_btn").off("click").click(rm_element);
    };
   
    var add_point = function(not_update) {
        $("#points").append('<tr><td><p class="x"></p></td>' + 
        '<td><input type="text" class="x" /></td>' + 
        '<td><p class="y"></p></td>' + 
        '<td><input type="text" class="y" /></td>' + 
        '<td><button type="button" class="rm_btn">Remove</button></td></tr>');
        
        if(not_update != true)
        {
            update_points();
        }
        
        $(".rm_btn").off("click").click(rm_element);
    };
    
    $("#graph").click();
});
