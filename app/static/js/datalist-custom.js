$(function() {
    $("form").on("input", "input[list=ingredients]",function()   {
        var selectedOption = $('option[value="'+$(this).val()+'"]');
        var ingredientFormField = $(this).parents().eq(1).prev("input");
        ingredientFormField.val(selectedOption.length ? selectedOption.attr('id') : "");
    });
});
