var form_count = 1;

$(function () {
        // add form functionality
        $("form").on("click", ".add_form", function (event) {
            const formSetDiv = $(this).parents(".form_set");
            const totalForms = formSetDiv.children("input:first");
            const emptyForm = formSetDiv.children(".empty_form");
            newForm = $.parseHTML(emptyForm.html().replace(/__prefix__/g, form_count))
            emptyForm.before(newForm)
            form_count++;
            totalForms.val(form_count);
            if (form_count > 1) {
                formSetDiv.children(".ingredient-container:first").children(".remove_form:first").show();
            }
        });

        // remove form functionality
        $("form").on("click", ".remove_form", function (event) {
            const formSetDiv = $(this).parents(".form_set");
            const formToBeRemoved = $(this).parents(".ingredient-container")
            formToBeRemoved.remove();
            form_count--;
            if (form_count === 1) {
                formSetDiv.children(".ingredient-container:first").children(".remove_form:first").hide();
            }
        });
});
