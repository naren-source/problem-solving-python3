friends = ["a", "b", "c", "d"]
for friend in friends:
    print(f"{friend} is my friend")

for n in range(4):
    print(f"{n} is a number")


# Average
grades = [55, 87, 23, 45, 99]
total = 0
no_of_students = len(grades)

for grade in grades:
    total += grade

print(f"The average of {no_of_students} students is {total/no_of_students}")
