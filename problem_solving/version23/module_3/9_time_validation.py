def validate_time(hours: int, minutes: int, seconds: int) -> str:
    return "VALID" if (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59) \
        else "NOT VALID"


number_of_inputs = int(input())
for i in range(number_of_inputs):
    value = [x for x in input().split("/")]
    given_time = {
        "hours": int(value[0]),
        "minutes": int(value[1]),
        "seconds": int(value[2])
    }
    print(validate_time(**given_time))


# ===========================================================
# Write a 'C' program to validate the given time
#
# Input Format
#
# First line tells the number of test cases Next lines represent the time hh/mm/ss
#
# Constraints
#
# NIL
#
# Output Format
#
# print VALID or NOT VALID
#
# Sample Input 0
#
# 3
# 12/30/45
# 23/45/12
# 45/67/34
# Sample Output 0
#
# VALID
# VALID
# NOT VALID
