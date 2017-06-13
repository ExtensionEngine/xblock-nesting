/* Javascript for NestingXBlock. */
function NestingXBlock(runtime, element, context) {

  $(function ($) {

    // Student view
    $(element).css({
      padding: context.styles.padding,
      border: context.styles.border
    });

    $(element).closest('.vert').css({
      width: 'calc(' + context.styles.width + ' - 3px)',
      display: 'inline-block',
      verticalAlign: 'top'
    });

  });
}
