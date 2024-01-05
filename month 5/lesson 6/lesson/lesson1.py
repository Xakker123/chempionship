def uching():
    n = 0
    for i in range(1, 10):
        yield 3 ** n
        n += 1


for i in uching():
    print(i)
