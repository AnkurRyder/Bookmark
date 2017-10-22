
title ="extension is working";

tag= "succes";

url="www.bookmarks.pythonanywhere.com";

 $(document).ready(function(){

    $("button").click(function(){

        

        $.ajax({

            type:'GET',

            url:'https://bookmarks.pythonanywhere.com/add_get',

            data:{

                'title':$('#title').val(),

                'tag':$('#tag').val(),

                'ur':$('#url').val(),

                },

            dataType: 'json',

            sucess:function(data){

                alert(" gf");

            },

        });

    });

});


        var text="untaged";
            $(function() {
  var list = $('.js-dropdown-list');
  var link = $('.js-link');
  link.click(function(e) {
    e.preventDefault();
    list.slideToggle(200);
  });
  list.find('li').click(function() {
    text = $(this).html();
    var icon = '<i class="fa fa-chevron-down"></i>';
    link.html(text+icon);
    list.slideToggle(200);

  });
});