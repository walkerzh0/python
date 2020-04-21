import os
import sys
import re
import handlers

class Rule:
    def condition(self, block):
        pass

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    type = 'heading'
    def condtion(self, block):
        return len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'title'
    first = True
    def condition(self, block):
        if self.first == True:
            self.first = False
            return HeadingRule.condition(self, block)
        else:
            return False

class ListItemRule(Rule):
    type = 'listitem'
    def condition(self, block):
        #print('listitem block: ' + block + 'hello')
        return block[0] == '-'
        #pass

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    type = 'list'
    inside = False
    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self, block):
        return True




