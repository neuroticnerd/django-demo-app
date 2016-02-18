(function(){
  $(window).scroll(function () {
    var top = $(document).scrollTop();
    if (top > 50) {
      $('.navbar').removeClass('navbar-transparent');
    } else {
      $('.navbar').addClass('navbar-transparent');
    }
  }).trigger('scroll');
})();
