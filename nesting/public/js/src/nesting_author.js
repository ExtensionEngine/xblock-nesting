function NestingAuthorXBlock(runtime, element, context) {

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        var $parent = $(element).parents('.studio-xblock-wrapper');
		if($parent.length) {
			$parent.css({
		    	width: context.width + '%',
		    	display: 'inline-block',
		    	verticalAlign: 'top'
		    });
		}
		else {
			$(element).css({
		    	width: context.width + '%',
		    	display: 'inline-block',
		    	verticalAlign: 'top'
		    });
		}
    });
}
