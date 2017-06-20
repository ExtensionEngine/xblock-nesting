DEFAULT_STYLES = {
  'margin': '0',
  'padding': '0',
  'border-top': '0',
  'border-right': '0',
  'border-bottom': '0',
  'border-left': '0'
}

DEFAULT_TEMPLATES = {
  'template-1': {
    'children': [
      {
        'category': 'video',
        'type': 'video',
        'children': []
      },
      {
        'id': 'nesting-1',
        'category': 'nesting',
        'width': 50,
        'children': [
          {
            'parent_id': 'nesting-1',
            'category': 'html',
            'children': []
          }
        ]
      },
      {
        'id': 'nesting-2',
        'category': 'nesting',
        'width': 50,
        'children': [
          {
            'parent_id': 'nesting-2',
            'category': 'html',
            'children': []
          }
        ]
      }
    ]
  },
  'template-2': {
    'children': [
      {
        'id': 'nesting-1',
        'category': 'nesting',
        'width': 70,
        'children': [
          {
            'parent_id': 'nesting-1',
            'category': 'html',
            'children': []
          },
          {
            'parent_id': 'nesting-1',
            'category': 'video',
            'type': 'video',
            'children': []
          },
          {
            'parent_id': 'nesting-1',
            'category': 'html',
            'children': []
          },
          {
            'id': 'nesting-3',
            'parent_id': 'nesting-1',
            'category': 'nesting',
            'width': 50,
            'children': [
              {
                'parent_id': 'nesting-3',
                'category': 'html',
                'children': []
              }
            ]
          },
          {
            'id': 'nesting-4',
            'parent_id': 'nesting-1',
            'category': 'nesting',
            'width': 50,
            'children': [
              {
                'parent_id': 'nesting-4',
                'category': 'html',
                'children': []
              }
            ]
          }
        ]
      },
      {
        'id': 'nesting-2',
        'category': 'nesting',
        'width': 30,
        'children': [
          {
            'parent_id': 'nesting-2',
            'category': 'html',
            'children': []
          },
          {
            'parent_id': 'nesting-2',
            'category': 'html',
            'children': []
          },
          {
            'parent_id': 'nesting-2',
            'category': 'html',
            'children': []
          },
          {
            'parent_id': 'nesting-2',
            'category': 'html',
            'children': []
          }
        ]
      }
    ]
  }
}
