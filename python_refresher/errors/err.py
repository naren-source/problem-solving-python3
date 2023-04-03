def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")

    return dividend/divisor


grades: [] = [1, 2, 4, 5, 8]

try:
    average: float = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("Grade list is empty")
else:
    print(f"The average of grades are {average}")
finally:
    print("Code execution ends")
