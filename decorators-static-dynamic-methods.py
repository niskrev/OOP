class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        try:
            return int(value)
        except:
            return 0
#        if isinstance(value, int):
#            return value
#        else:
#            return 0

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val
    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13.3)
c = InstanceCounter("hello")

for obj in (a, b, c):
    print('val of obj: {}'.format(obj.get_val()))
    print('count: {}'.format(obj.get_count()))
print(InstanceCounter.count)
