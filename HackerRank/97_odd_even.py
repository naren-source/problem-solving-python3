def findOddEven(n: int) -> None:
    odd = 0
    even = 0
    while n:
        r = n % 10
        if r % 2 == 0:
            even += 1
        else:
            odd += 1
        n = int(n/10)
    print(f"{odd},{even}")


findOddEven(int(input()))

# Given a number, find the number of odd and even digits
#
# Input Format
#
# Input is an integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# first odd and even %d %d
#
# Sample Input 0
#
# 1234567
# Sample Output 0
#
# 4,3