class MaxSizeList(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.list = []

    def push(self, element):
        self.list.append(element)
        if len(self.list) > self.maxsize:
            self.list.pop(0)

    def get_list(self):
        return self.list
