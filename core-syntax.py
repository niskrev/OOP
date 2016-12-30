class SumList(object):

    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        return SumList([x+y for x, y in zip(self.mylist, other.mylist)])

    def __repr__(self):
        return str(self.mylist)


cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

print(cc + dd)

print([1, 2, 3, 4, 5] + [100, 200, 300, 400, 500])
