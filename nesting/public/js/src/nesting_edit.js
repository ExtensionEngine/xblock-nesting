function NestingEditXBlock(runtime, element, context) {
	$(element).on('click', '.save-button', function() {
        var el = $(element);
        var data = {
            width: el.find('input[id=width]').val(),
        };         
        $.post(runtime.handlerUrl(element, 'studio_submit'), JSON.stringify(data)).done(function(response) {
            window.location.reload(false);
        });
    });

    $(element).on('click', '.cancel-button', function() {
        runtime.notify('cancel', {});
    });
};