def validate_date(date: int, month: int, year: int) -> str:
    if 1900 <= year <= 2200:
        if 0 < month <= 12:
            if (month == 2 and (date == 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else date == 28)) \
                    or (month > 7 and (0 < date <= 31 if month % 2 == 0 else 0 < date <= 30)) \
                    or (month <= 7 and (0 < date <= 31 if month % 2 != 0 else 0 < date <= 30)):
                return "VALID"
    return "NOT VALID"


number_of_inputs = int(input())
for i in range(number_of_inputs):
    value = [x for x in input().split("/")]
    given_date = {
        "date": int(value[0]),
        "month": int(value[1]),
        "year": int(value[2])
    }
    print(validate_date(**given_date))


# ==============================================================================
# Write a program to validate the given date
#
# Input Format
#
# First line represents the test case and the following lines will have the date to validate
#
# Constraints
#
# 1900 ≤ year ≤ 2200
#
# Output Format
#
# print VALID or NOT VALID
#
# Sample Input 0
#
# 3
# 12/4/2015
# 32/8/2016
# -12/1/2000
# Sample Output 0
#
# VALID
# NOT VALID
# NOT VALID
