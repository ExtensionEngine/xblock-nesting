function NestingAuthorXBlock(runtime, element, context) {

  $(function ($) {
    var $parent = $(element).closest('.studio-xblock-wrapper');

    if($parent.length) {
      $parent.css({
        width: 'calc(' + context.width + '% - 3px)',
        display: 'inline-block',
        verticalAlign: 'top',
      });
    }
    else {
      // Element seen in Author view (Nesting XBlock that is inside another Nesting XBlock)
      $(element).css({
        width: 'calc(' + context.width + '% - 3px)',
        display: 'inline-block',
        verticalAlign: 'top',
        boxSizing: 'border-box',
      }).css(context.styles);
    }

    /*
    for(var i=0; i<5; i++){
      $(element).next().remove();
    }
    */
  });
}
