'''
def show():
    return 1
    return 2
print(show())

'''
def show():
    yield 1
    yield 2
    yield 3
for i in show():
    print(i)

show()