$(window).on('load', function() {
    var ingredientValueField = $("input[list=ingredients]");
    ingredientValueField.each(function () {
        var ingredientFormField = $(this).parents().eq(1).prev("input");
        var selectedOption = $('option[value="'+$(this).val()+'"]');
        if (ingredientFormField.val() === "")   {
            ingredientFormField.val(selectedOption.attr("id"));
        }
    });
});


$(function() {
    $("form").on("input", "input[list=ingredients]",function()   {
        var selectedOption = $('option[value="'+$(this).val()+'"]');
        var ingredientFormField = $(this).parents().eq(1).prev("input");
        ingredientFormField.val(selectedOption.length ? selectedOption.attr("id") : "");
    });
});
