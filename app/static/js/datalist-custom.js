$(function() {
    $("input[list=ingredients]").on("input",function() {
        var selectedOption = $('option[value="'+$(this).val()+'"]');
        var ingredientFormField = $(this).parents().eq(1).prev("input");
    });
});
