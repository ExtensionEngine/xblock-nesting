function NestingEditXBlock(runtime, element, context) {
  var locator = $(element).parent().data('locator');
  var $el = $(element);

  // List of templates to be saved.
  var template_list = []
  // Dictionary of parent locators.
  var locators = {}
  // List of nesting XBlocks
  var nesting_xblocks = []
  // Counter variables.
  var i = 0, j = 0;
  // XBlock data to be saved in studio_submit.
  var xblock_data = {};

  $el.on('click', '.add-template-btn', function() {
    var selected_template = $(this).data('template');
    prepareData();
    // Convert template tree to list of XBlocks.
    traverseTreeToList(context.templates[selected_template]);
    // Remove root object.
    template_list.shift();

    // Create XBlocks from template_list.
    createXBlocks();
  });

  $el.on('click', '.save-button', function() {
    prepareData();
    studioSubmit();
  });

  $(element).on('click', '.cancel-button', function() {
    runtime.notify('cancel', {});
  });

  function prepareData() {
    // Hide 'Save' button and display spinner icon.
    $('.save-button').addClass('no-display');
    $('.spinner').removeClass('no-display');

    // Prepare data for saving.
    var styles = {}
    $el.find('.input-container input[data-style]').each(function(){
      var key = $(this).data('style');
      styles[key] = $(this).val();
    })     
    
    xblock_data = {
      width: $el.find('input[id=width]').val(),
      styles: styles
    }
  };

  function traverseTreeToList(template) {
    var queue = [];
    queue.push(template);
    currentTree = queue.shift();

    while(currentTree){
      for (var i = 0, length = currentTree.children.length; i < length; i++) {
        queue.push(currentTree.children[i]);
      }
      template_list.push(currentTree)
      currentTree = queue.shift();
    }
  };

  function createXBlocks() {
    if(i == template_list.length){
      setNestingXBlocks();
      return; //last call was last item in the array
    } 
    $.ajax({
      url:'/xblock/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        parent_locator: template_list[i].parent_id ? locators[template_list[i].parent_id] : locator,
        category: template_list[i].category,
        type: template_list[i].type
      }),
      success: function(data){
        if(template_list[i].category == 'nesting'){
          // Save locator for child elements.
          locators[template_list[i].id] = data.locator;

          template_list[i].locator = data.locator;
          nesting_xblocks.push(template_list[i]);
        }
        i++;
        createXBlocks();
      }
    });
  };

  function setNestingXBlocks() {
    if(j == nesting_xblocks.length){
      studioSubmit();
      return; //last call was last item in the array
    } 
    $.ajax({
      url:'/xblock/' + nesting_xblocks[j].locator + '/handler/studio_submit',
      type: 'POST',
      data: JSON.stringify({
        width: nesting_xblocks[j].width,
        styles: context.styles
      }),
      success: function(){
        j++;
        setNestingXBlocks();
      }
    });
  };

  function studioSubmit() {
    $.post(runtime.handlerUrl(element, 'studio_submit'), JSON.stringify(xblock_data)).done(function(response) {
      window.location.reload(false);
    });
  };
};
