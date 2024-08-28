def set_it_right(n: int, o: int) -> str:
    odd = ""
    even = ""
    while n:
        x = n % 10
        if x % 2 == 0:
            even = f"{x}{even}"
        else:
            odd = f"{x}{odd}"
        n = int(n/10)
    return f"{odd}{even}" if o == 1 else f"{even}{odd}"


num, order = input().split()
print(set_it_right(int(num), int(order)))


# Write a function set_it_right(long long num, int operation)
#
# I/P 123456789, 0 O/P 246813579
#
# I/P 90134723, 1 O/P 91373042
#
# Input Format
#
# 0 - even first odd second 1 - odd first even second
#
# Constraints
#
# should right the function
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 123456789 0
# Sample Output 0
#
# 246813579
# Sample Input 1
#
# 900123445 0
# Sample Output 1
#
# 002449135
