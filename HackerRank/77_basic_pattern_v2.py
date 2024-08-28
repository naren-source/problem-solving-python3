def generatePattern(lines: int, start: int) -> None:
    count = start
    for x in range(1, lines+1):
        for y in range(1, x+1):
            print(count, end="")
        count += 1
        print()
    for x in range(lines, 0, -1):
        count -= 1
        for y in range(x):
            print(count, end="")
        print()


testCase = int(input())
for tc in range(testCase):
    lines, start = input().split()
    generatePattern(int(lines), int(start))


# Write a program to print the pattern .when n=4 and s=3 3
# 44
# 555
# 6666
# 6666
# 555
# 44
# 3
#
# Input Format
#
# First line denotes the number of test cases. Each line contains two integers n and s
#
# Constraints
#
# 1 ≤ n,s ≤ 100
#
# Output Format
#
# print the pattern. leave an empty line for each test case
#
# Sample Input 0
#
# 3
# 3 4
# 5 2
# 4 1
# Sample Output 0
#
# 4
# 55
# 666
# 666
# 55
# 4
#
# 2
# 33
# 444
# 5555
# 66666
# 66666
# 5555
# 444
# 33
# 2
#
# 1
# 22
# 333
# 4444
# 4444
# 333
# 22
# 1