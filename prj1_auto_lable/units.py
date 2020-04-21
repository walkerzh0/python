import os
import sys

class Units:
    def __init__(self):
        self.file = ''

    def lines(self):
        #print('lines file is: ', self.file)
        doc = open(self.file, 'r')
        while True:
            line = doc.readline()
            if line:
                yield line
            else:
                break
        doc.close()

    def blocks(self, file):
        self.file = file
        #print('block file is: ', self.file)
        blockdata = []
        for line in self.lines():
            if line:
                blockdata.append(line.strip())
                if line.strip():
                    pass
                else:
                    yield ''.join(blockdata)
                    blockdata = []



units = Units()

#for block in units.blocks('doc.txt'):
#    print('------------------------------------------------------')
#    print(block)