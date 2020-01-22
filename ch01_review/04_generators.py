def generator(max):
    for i in range(max):
        yield i
    return

g = generator(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
