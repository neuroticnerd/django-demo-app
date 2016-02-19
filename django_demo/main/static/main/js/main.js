(function(){
  var tooltipDelay = 500;

  $(window).scroll(function () {

    var top = $(document).scrollTop();
    if (top > 50) {
      $('.navbar').removeClass('navbar-transparent');
    } else {
      $('.navbar').addClass('navbar-transparent');
    }

  }).trigger('scroll');

  $('[data-toggle="tooltip"]').tooltip({
    container: 'body',
    delay: { "show": tooltipDelay, "hide": 0 },
  });

  var loginModal = $('#login-modal');
  var usernameField = $('#id_username');

  loginModal.on('shown.bs.modal', function () {
    usernameField.focus();
  });

  $('a[data-target="#login-modal"]').on('click', function () {
    loginModal.modal('toggle');
    return false;
  });

  var loginForm = $('.form-login');
  var inputs = loginForm.find('.form-group > div > input.form-control');
  inputs.attr('size', 40);

})();
