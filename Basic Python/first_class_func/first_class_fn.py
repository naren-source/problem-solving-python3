def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("No divisor")

    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


print(calculate(20, 4, operator=divide))
