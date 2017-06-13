function NestingEditXBlock(runtime, element, context) {
  var $el = $(element);

  $el.on('click', '.save-button', function() {
    var styles = {}

    $el.find('.input-container').each(function(){
      var input= $(this).find('input');
      var key = $(this).find('input').data('style');
      styles[key] = $(input).val();
    })     

    $.post(runtime.handlerUrl(element, 'studio_submit'), JSON.stringify(styles)).done(function(response) {
      window.location.reload(false);
    });
    
  });

  $(element).on('click', '.cancel-button', function() {
    runtime.notify('cancel', {});
  });
};