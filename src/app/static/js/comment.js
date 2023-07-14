$(document).ready(function(){
    const commentSection = $(".comments-list");
    const emptyComment = $("#comment_empty .media");

    function addCommentToList(user, date, text) {
        let newComment = emptyComment.clone();
        newComment.find("h4.user_name").prepend(user);
        newComment.find("h4.user_name small").text(date);
        newComment.find("p").append(text);
        return newComment;
    }

    $(".comment-form").on("click", "button", function(event){
        event.preventDefault();
        let recipe_id = $(this).parents("form").attr("value");
        let text = $(this).prev("textarea");
        let data = {
            "recipe": recipe_id,
            "text": text.val(),
        };
        $.ajax({
            type: "POST",
            headers:{
                "X-CSRFToken": csrfToken,
            },
            url: createCommentUrl,
            data: data,
            success: function(data){
                text.val('');
                let newComment = addCommentToList(currentUser, "Just now", data.text);
                commentSection.prepend(newComment);
                $('html, body').animate({
                    scrollTop: newComment.offset().top
                }, 2000);
            },
            error: function(rs, e){
              console.log(rs.responseText);
            }
        });
    });

    let visible = 5;

    function getComments(visible) {
        $.ajax({
            type: "GET",
            url: commentListUrl + "?visible=" + visible,
            success: function(data)  {
                data.forEach(function(obj) {
                    let newComment = addCommentToList(obj.user, obj.date, obj.text);
                    commentSection.append(newComment);
                })
                if (visible >= commentListLength) {
                    $(".load-button").attr("hidden", true);
                }
            },
            error: function(rs, e){
              console.log(rs.responseText);
            }
        });
    };

    getComments(visible);

    $(".load-button").on("click", "button", function(event){
        visible += 5;
        getComments(visible);
    });
})
