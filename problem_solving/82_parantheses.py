def checkParantheses(iStr: str) -> int:
    open, close = '(', ')'
    counter = 0
    pair = 0
    for char in iStr:
        if char == open:
            counter += 1
            pair += 1
        elif char == close:
            counter -= 1
        else:
            return -1
    if counter == 0:
        return pair
    else:
        return -1


pair = checkParantheses(input())
if pair > 0:
    print(f"Balanced {pair}")
else:
    print("Not Balanced")

# Test whether an input string of opening and closing parentheses was balanced or not. If yes , return the no. of parentheses. If no, return -1.
#
# Ip: “(( ))” Op: 2 Ip: “()(“ Op:-1
#
# Input Format
#
# Given a string
#
# Constraints
#
# 1 7le; string_length ≤ 1000
#
# Output Format
#
# If the returned value is -1 print Not balanced if not, print Balanced ** and the **count.
#
# Sample Input 0
#
# ((()))
# Sample Output 0
#
# Balanced 3
# Sample Input 1
#
# (([]
# Sample Output 1
#
# Not Balanced
