import random
from io import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "this is a silly message"
        self.writer.write(write_text)

with open("test.txt", "w") as fh:
    w1 = WriteMyStuff(fh)
    w1.write()

sioh = StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print('file object: ', open('test.txt', 'r').read())
print('StringIO object: {}'.format(sioh.getvalue()))
