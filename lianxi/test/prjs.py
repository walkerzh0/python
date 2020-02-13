# 自动添加标签
import sys, re

def lines(file):
    #print("lines file is :", file)
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    #print("blocks file is :", file)
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

import sys, re
from prjs import  *
# print("Hello1")
# blocks(sys.stdin)
# print("Hello2")

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)

    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')