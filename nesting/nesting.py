import pkg_resources
import logging

from xblock.core import XBlock
from xblock.fields import Scope, String, Integer, Dict
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioContainerXBlockMixin
from xblockutils.resources import ResourceLoader

from .default_data import DEFAULT_STYLES
from .default_data import DEFAULT_TEMPLATES

loader = ResourceLoader(__name__)

class NestingXBlock(StudioContainerXBlockMixin, XBlock):

    display_name = String(
        display_name='Title',
        default='Nesting XBlock',        
        scope=Scope.settings,
        help='The title of the Nesting XBlock. The title is displayed to learners.',
    )

    width = Integer(
        display_name='XBlock width',
        default=100,
        scope=Scope.settings,
        help='Width of Nesting XBlock defined in percentages.'
    )

    styles = Dict(
        display_name='XBlock styles',
        default=DEFAULT_STYLES,
        scope=Scope.settings,
        help='XBlock styles.'
    )

    templates = Dict(
        display_name='XBlock templates',
        default=DEFAULT_TEMPLATES,
        scope=Scope.settings,
        help='Default XBlock templates.'
    )

    has_children = True

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    def studio_view(self, context=None):
        context = {
            'display_name': self.display_name,
            'width': self.width,
            'styles': self.styles,
            'templates': self.templates
        }
        frag = Fragment()
        frag.add_content(loader.render_template('/public/html/nesting_edit.html', context))
        frag.add_css(self.resource_string('public/css/nesting_edit.css'))
        frag.add_javascript(self.resource_string('public/js/src/nesting_edit.js'))
        frag.initialize_js('NestingEditXBlock', context)
        return frag

    def student_view(self, context=None):
        context = {
            'display_name': self.display_name,
            'width': self.width,
            'styles': self.styles
        }
        frag = Fragment()
        self.render_children(context, frag, can_reorder=False, can_add=False)
        frag.add_css(self.resource_string('public/css/nesting.css'))
        frag.add_javascript(self.resource_string('public/js/src/nesting.js'))
        frag.initialize_js('NestingXBlock', context)
        return frag

    def author_view(self, context):
        context = {
            'display_name': self.display_name,
            'width': self.width,
            'styles': self.styles
        }
        frag = Fragment()
        self.render_children(context, frag, can_reorder=True, can_add=True)
        frag.add_css(self.resource_string('public/css/nesting.css'))
        frag.add_javascript(self.resource_string('public/js/src/nesting_author.js'))
        frag.initialize_js('NestingAuthorXBlock', context)
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        self.width = data.get('width')
        self.styles = data.get('styles')

        return {'result': 'success'}
