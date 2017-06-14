function NestingEditXBlock(runtime, element, context) {

  var $el = $(element);

  $el.on('click', '.save-button', function() {

    var styles = {}
    $el.find('.input-container input[data-style]').each(function(){
      var key = $(this).data('style');
      styles[key] = $(this).val();
    })     

    var data = {
      width: $el.find('input[id=width]').val(),
      styles: styles
    }

    $.post(runtime.handlerUrl(element, 'studio_submit'), JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
    });
    
  });

  $(element).on('click', '.cancel-button', function() {
    runtime.notify('cancel', {});
  });
};