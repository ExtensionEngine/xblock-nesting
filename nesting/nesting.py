import pkg_resources
import logging

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioContainerXBlockMixin
from xblockutils.resources import ResourceLoader

loader = ResourceLoader(__name__)

class NestingXBlock(StudioContainerXBlockMixin, XBlock):

    display_name = String(
        display_name="Title",
        default="Nesting XBlock",        
        scope=Scope.settings,
        help="The title of the Nesting XBlock. The title is displayed to learners.",
    )

    width = Integer(
        display_name="XBlock Width",
        default=100,
        scope=Scope.settings,
        help="Defining the width of the XBlock.",
    )

    has_children = True

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def studio_view(self, context=None):
        context = {
            'width': self.width
        }
        frag = Fragment()
        frag.add_content(loader.render_template('/public/html/nesting_edit.html', context))
        frag.add_css(self.resource_string("public/css/nesting_edit.css"))
        frag.add_javascript(self.resource_string("public/js/src/nesting_edit.js"))
        frag.initialize_js('NestingEditXBlock', context)
        return frag

    def student_view(self, context=None):
        context = {
            'width': self.width
        }
        frag = Fragment()
        self.render_children(context, frag, can_reorder=False, can_add=False)
        frag.add_content(loader.render_template('/public/html/nesting.html', context))
        frag.add_css(self.resource_string("public/css/nesting.css"))
        frag.add_javascript(self.resource_string("public/js/src/nesting.js"))
        frag.initialize_js('NestingXBlock', context)
        return frag

    def author_edit_view(self, context):
        """
        View used by StudioContainerXBlockMixin to render content customize author_view
        """
        context = {
            'width': self.width
        }
        html = self.resource_string("public/html/nesting_author_edit.html").format(self=self)
        frag = Fragment(html.format(self=self))
        self.render_children(context, frag, can_reorder=True, can_add=True)
        frag.add_css(self.resource_string("public/css/nesting.css"))
        frag.add_javascript(self.resource_string("public/js/src/nesting_author_edit.js"))
        frag.initialize_js('NestingAuthorEditXBlock', context)
        return frag

    def author_view(self, context):
        context = {
            'width': self.width
        }
        frag = Fragment()
        self.render_children(context, frag, can_reorder=True, can_add=True)
        frag.add_content(loader.render_template('/public/html/nesting_author.html', context))
        frag.add_css(self.resource_string("public/css/nesting.css"))
        frag.add_javascript(self.resource_string("public/js/src/nesting_author.js"))
        frag.initialize_js('NestingAuthorXBlock', context)
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        self.width = data.get('width')

        return {'result': 'success'}
