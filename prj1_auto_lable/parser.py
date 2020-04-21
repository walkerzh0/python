from units import *
from handlers import *
from rules import *


class Parser:
    def __init__(self, file, handler):
        self.file = file
        self.rules = []
        self.filters = []
        self.handler = handler

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_filter(self, pattern, name):
        def filter(block, handler):
            re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parser(self):
        #print('Parser file is: ', self.file)
        self.handler.start('document')
        for block in units.blocks(self.file):
            for filter in self.filters:
                filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicParser(Parser):
    def __init__(self, file, handler):
        super().__init__(file, handler)
        self.add_filter(r'\*(.+?)\*', 'emphasis')
        self.add_filter(r'(http://[\.a-zA-Z0-9]+)', 'url')
        self.add_filter(r'([\.a-zA-A0-9]+@[\.a-zA-Z0-9]+[a-zA-Z0-9]+)', 'email')

        self.add_rule(ListRule())
        self.add_rule(ListItemRule())
        self.add_rule(TitleRule())
        self.add_rule(HeadingRule())
        self.add_rule(ParagraphRule())


mHandler = HtmlHandler()
mParser = BasicParser('doc.txt', mHandler)
mParser.parser()





