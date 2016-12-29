import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0
    def set_val(self, value):
        self.val = value
    def get_val(self):
        return self.val
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)
    def showdoc(self):
        print('GetSetInt object ({0}), only accepts '
         'integer values'.format(id(self)))

class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print('GetSetList object ({0}), stores '
        'history of values set'.format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()
y = GetSetList('a')
y.set_val('b')
print(y.get_val())
print(y.get_vals())
y.set_val('c')
print(y.get_vals())




