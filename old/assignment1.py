from assignments.max_size_list import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push(1)
a.push(2)
a.push(3)
a.push(4)

b.push(1)
b.push(2)
b.push(3)

print(a.get_list())
print(b.get_list())

