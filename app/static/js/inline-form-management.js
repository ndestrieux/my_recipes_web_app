$(document).ready(function () {
    $(".form_set .ingredient-container:not(:last-child) label.requiredField").next("div").children("input.form-control").attr("required", "");
    var form_count = $(".form_set input[name=ingredientquantity_set-TOTAL_FORMS]").val();
    if (form_count > 1) {
        $(".form_set .ingredient-container:not(:last-child)").children(".remove_form").show();
    }

    $(function () {
        // add form functionality
        $("form").on("click", ".add_form", function (event) {
            const formSetDiv = $(this).parents(".form_set");
            const totalFormsElement = formSetDiv.children("input[name=ingredientquantity_set-TOTAL_FORMS]");
            const totalForms = parseInt(totalFormsElement.val());
            const emptyForm = formSetDiv.children(".empty_form");
            newForm = $.parseHTML(emptyForm.html().replace(/__prefix__/g, totalForms));
            emptyForm.before(newForm);
            form_count++;
            totalFormsElement.val(totalForms + 1);
            if (form_count > 1) {
                formSetDiv.children(".ingredient-container:first").children(".remove_form:first").show();
            }
        });

        // remove form functionality
        $("form").on("click", ".remove_form", function (event) {
            const formSetDiv = $(this).parents(".form_set");
            const formToBeRemoved = $(this).parents(".ingredient-container");
            formToBeRemoved.remove();
            form_count--;
            if (form_count === 1) {
                formSetDiv.children(".ingredient-container:first").children(".remove_form:first").hide();
            }
        });
    });
});




