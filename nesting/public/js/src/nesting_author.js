function NestingAuthorXBlock(runtime, element, context) {

  $(function ($) {
    var $parent = $(element).closest('.studio-xblock-wrapper');
    if($parent.length) {

      $parent.css({
        width: 'calc(' + context.styles.width + ' - 3px)',
        display: 'inline-block',
        verticalAlign: 'top'
      });
      
    }
    else {
      $(element).css({
        width: 'calc(' + context.styles.width + ' - 3px)',
        display: 'inline-block',
        verticalAlign: 'top'
      });
    }

    /*
    for(var i=0; i<5; i++){
      $(element).next().remove();
    }
    */
  });
}
