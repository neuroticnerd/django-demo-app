(function(){
  var tooltipDelay = 500;

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

})();
