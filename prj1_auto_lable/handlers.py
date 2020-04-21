import re
import os
import sys

class Handler:
    def __init__(self):
        pass

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
        return substitution


class HtmlHandler(Handler):
    def __init__(self):
        super().__init__()

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_heading(self):
        print('<h1>')

    def end_heading(self):
        print('</h1>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_titile(self):
        print('<title>')

    def end_title(self):
        print('</title>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_email(self, match):
        return '<a ="mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)

