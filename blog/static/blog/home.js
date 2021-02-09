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

         if(data["result"] == "Liked+1"){
            $( '#likebutton'+ catid ).removeClass("far");
            $( '#likebutton'+ catid ).addClass("fa");
         }
         else if(data["result"] == "Liked-1"){
            $( '#likebutton'+ catid ).removeClass("fa");
            $( '#likebutton'+ catid ).addClass("far");
            $( '#likebutton'+ catid ).css({"font-size": "170%"});
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

         if(data["result"] == "DisLiked+1"){
            $( '#dislikebutton'+ catid ).removeClass("far");
            $( '#dislikebutton'+ catid ).addClass("fa");
         }
         else if(data["result"] == "DisLiked-1"){
            $( '#dislikebutton'+ catid ).removeClass("fa");
            $( '#dislikebutton'+ catid ).addClass("far");
            $( '#dislikebutton'+ catid ).css({"font-size": "170%"});
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
            $( '#favorite'+ catid ).removeClass("fa-bookmark-o");
            $( '#favorite'+ catid ).addClass("fa-bookmark");
         }
         else{
            $( '#favorite'+ catid ).removeClass("fa-bookmark");
            $( '#favorite'+ catid ).addClass("fa-bookmark-o");
         }
        }
    })
    });