def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 5, 7))


def add(x, y):
    return x+y


nums = [1, 2]
print(add(*nums))


def apply(*args, operator):
    print(args)
    print(*args)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 3, 5, 6, operator="*"))
