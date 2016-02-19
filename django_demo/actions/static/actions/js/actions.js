(function(){
  var actionModal = $('#action-detail-modal');
  alert(actionModal.text());

  actionModal.on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    alert(button.text());
    var action = button.data('action');
    alert(action);
    var modal = $(this);
    modal.find('.modal-body').html(action);
  });

})();
