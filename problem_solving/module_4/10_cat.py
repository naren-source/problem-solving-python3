def calc(n: int, operand: str) -> int:
    total = 0 if operand == "+" else 1
    while n:
        r = n % 10
        if operand == "+":
            total += r
        else:
            total *= r
        n = int(n/10)
    return total


def check_cat(n: int) -> str:
    num = n
    str_list = [""] * 3
    count = 0
    return_string = ""
    total = calc(n, "+") * calc(n, "*")
    if total == n:
        while n:
            str_list[len(str_list) - 1 - count] = n % 10
            n = int(n / 10)
            count += 1
        return_string = f"{num} = ({str_list[0]}+{str_list[1]}+{str_list[2]})*({str_list[0]}*{str_list[1]}*{str_list[2]})"
    return return_string


print(check_cat(135))



# ================================================================
# Write a 'C' program to check the following condition. CAT = (C+A+T)* (C*A*T) where as each letter is a digit
#
# Input Format
#
# NIL
#
# Constraints
#
# NIL
#
# Output Format
#
# print the value CAT = (C+A+T)* (C*A*T)
#
# Sample Output 0
#
# 135 = (1+3+5)*(1*3*5)
