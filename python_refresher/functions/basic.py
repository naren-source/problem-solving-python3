def hello():
    print("Hello")


hello()


def add_friends():
    friend_name = input("Enter name")
    f = friends + [friend_name]


friends = ["a", "b"]
add_friends()
# friends = ["a", "b"]


def add(x, y=5):
    print(x+y)


add(1)
add(1, 2)


def addx(x,y):
    return x+y


print(addx(5, 8))
