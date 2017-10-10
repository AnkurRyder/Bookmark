
$(document).ready(function() {

  setTimeout(function() {
    $('.ball').addClass('scale');
  }, 1000);

  setTimeout(function() {
    $('.user-photo').addClass('user-photo-animate');
  }, 1200);

  setTimeout(function() {
    $('.user-photo-mask > img').addClass('user-img');
    $('.user-photo-mask > img').addClass('user-img');
  }, 1400);

  setTimeout(function() {
    $('.user-name').addClass('fadeInUp');
  }, 1500);

  setTimeout(function() {

    var children = $("ul.lines > li");
    var index = 0;
    //console.log(children);

    function addClassNextChild() {
      if (index == children.length) return;
      children.eq(index++).addClass('fadeInUp');
      window.setTimeout(addClassNextChild, 200);
    }
    addClassNextChild();
  }, 1600);

}); //end Document ready