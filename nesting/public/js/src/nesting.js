/* Javascript for NestingXBlock. */
function NestingXBlock(runtime, element, context) {

  $(function ($) {
    // Element seen in Student view
    $(element).css(context.styles);

    $(element).closest('.vert').css({
      width: 'calc(' + context.width + '% - 3px)',
      boxSizing: 'border-box',
      display: 'inline-block',
      verticalAlign: 'top'
    });
  });
}
