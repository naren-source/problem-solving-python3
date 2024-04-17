number = 7
user_input = input("Would you like to guess ? ")
positive_answers = ['y', 'Y', 'yes', 'Yes']
count = 3
while user_input in positive_answers:
    count -= 1
    if count < 0:
        break
    user_number = int(input("Guess the number?"))
    if user_number == number:
        print("You are correct!!")
    elif abs(user_number - number) == 1:
        print("Pretty Close!!")
    else:
        print("Better luck next Time")

