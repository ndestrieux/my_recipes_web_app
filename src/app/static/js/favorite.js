$(document).ready(function(){
    $(".appreciation-form").on("click", ".favorite", function(event){
        event.preventDefault();
        let recipe_id = $(this).parents("form").attr("value");
        let favorite
        if ($(this).hasClass("active")) {
            $(this).removeClass("active");
            favorite = false;
        } else {
            $(this).addClass("active");
            favorite = true;
        }
        let data = {
            "is_favorited_by": favorite,
        };
        $.ajax({
            type: "PUT",
            headers:{
                "X-CSRFToken": csrfToken,
            },
            url: favoriteUrl,
            data: data,
            error: function(rs, e){
              console.log(rs.responseText);
            }
        });
    });
})
