def orderTheNumbers(num: int, ord: int) -> int:
    oddSeq = 0
    evenSeq = 0
    oPwr = 0
    ePwr = 0
    while num:
        last = num % 10
        if last % 2 == 0:
            evenSeq += (last*(10**ePwr))
            ePwr += 1
        else:
            oddSeq += (last*(10**oPwr))
            oPwr += 1
        num /= 10
        num = int(num)
    return (evenSeq*(10**oPwr) + oddSeq) if ord == 1 else (oddSeq*(10**ePwr) + evenSeq)


order, number = input().split(' ')
print(orderTheNumbers(int(number), int(order)))


# Write a 'C' program to arrange the even digits first and odd digits second of the given number vice versa.
#
# Input Format
#
# First input is option and next the value If the option is 0 - odd digits first 1 - even digits first
#
# Constraints
#
# 1 ≤ num ≤ 100000007
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 0 89745
# Sample Output 0
#
# 97584
