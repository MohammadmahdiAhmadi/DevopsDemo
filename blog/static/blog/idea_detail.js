$('.likebutton').click(function(){
    var catid;
    catid = $(this).attr("name");
    $.ajax(
      {
       type:"GET",
        url: "/likeIdea",

       data:{
         idea_id: catid
       },

       success: function( data ){
         //$( '#like'+ catid ).text(data["number_of_likes"]);

         if(data["result"] == "Liked+1"){
            $( '.likebutton' ).removeClass("far");
            $( '.likebutton' ).addClass("fa");
         }
         else if(data["result"] == "Liked-1"){
            $( '.likebutton' ).removeClass("fa");
            $( '.likebutton' ).addClass("far");
            $( '.likebutton' ).css({"font-size": "170%"});
         }
        }
    })

  });
  $('.dislikebutton').click(function(){
    var catid;
    catid = $(this).attr("name");
    $.ajax(
      {
       type:"GET",
        url: "/dislikeIdea",

       data:{
         idea_id: catid
       },

       success: function( data ){
         //$( '#dislike'+ catid ).text(data["number_of_dislikes"]);

         if(data["result"] == "DisLiked+1"){
            $( '.dislikebutton' ).removeClass("far");
            $( '.dislikebutton' ).addClass("fa");
         }
         else if(data["result"] == "DisLiked-1"){
            $( '.dislikebutton' ).removeClass("fa");
            $( '.dislikebutton' ).addClass("far");
            $( '.dislikebutton' ).css({"font-size": "170%"});
         }
        }
    })

  });
  $('.favorite').click(function(){
    var catid;
    catid = $(this).attr("name");
    $.ajax(
      {
       type:"GET",
        url: "/favorite",

       data:{
         idea_id: catid
       },

       success: function( data ){
         if(data == "Saved"){
            $( '.favorite' ).removeClass("fa-bookmark-o");
            $( '.favorite' ).addClass("fa-bookmark");
         }
         else{
            $( '.favorite' ).removeClass("fa-bookmark");
            $( '.favorite' ).addClass("fa-bookmark-o");
         }
        }
    })

  });