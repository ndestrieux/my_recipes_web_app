$(document).ready(function(){
    $(".appreciation-form").on("click", ".vote", function(event){
        event.preventDefault();
        let recipe_id = $(this).parents("form").attr("value");
        if ($(this).hasClass("active")) {
            $(this).removeClass("active");
        } else {
            $(".vote").removeClass("active");
            $(this).addClass("active");
        }
        let data = {
                "recipe": recipe_id,
                "vote": $(this).attr("value"),
        };
        $.ajax({
            type: "POST",
            headers:{
                "X-CSRFToken": csrfToken,
            },
            url: voteUrl,
            data: data,
            success: function(){
                let ranking_html = $("#likeCounter");
                fetch(rankingUrl, {
                    headers:{
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                })
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    ranking_html.html(data["up"] - data["down"]);
                })
            },
            error: function(rs, e){
              console.log(rs.responseText);
            }
        });
    });
})
