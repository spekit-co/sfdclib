"""Contains utility methods and classes for the library.
"""

from xml.etree import ElementTree


class CommentedTreeBuilder(ElementTree.TreeBuilder):
    """Parser class that includes comments. Based on:
    https://stackoverflow.com/questions/33573807/faithfully-preserve-comments-in-parsed-xml-python-2-7
    """

    def __init__(self, *args, **kwargs):
        super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

    def comment(self, data):
        self.start(ElementTree.Comment, {})
        self.data(data)
        self.end(ElementTree.Comment)
