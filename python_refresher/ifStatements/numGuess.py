number = 7
user_input = input("Would you like to guess ? ")
positive_answers = ['y', 'Y', 'yes', 'Yes']

if user_input in positive_answers:
    user_number = int(input("Guess the number?"))
    if user_number == number:
        print("You are correct!!")
    elif abs(user_number - number) == 1:
        print("Pretty Close!!")
    else:
        print("Better luck next Time")
else:
    print("Thanks!!")
