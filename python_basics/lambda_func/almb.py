add = lambda x, y: x+y
print(add(1, 2))
print((lambda x, y: x+y)(1, 2))

sequence = [1, 2, 3, 4, 5]
doubled = [x*2 for x in sequence]
print(doubled)


def triple(x):
    return x*3


tripled = [triple(x) for x in sequence]
print(tripled)

doubledx = [(lambda x:x*2)(x) for x in sequence]
print(doubledx)


triplex = list(map(triple, sequence))
print(triplex)

tripley = list(map(lambda x: x*4, sequence))
print(tripley)
