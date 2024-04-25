def formLargest(nList: list, listSize: int) -> int:
    largestNum = 0
    for x in range(listSize):
        for y in range(listSize-1-x):
            if nList[y] > nList[y+1]:
                temp = nList[y]
                nList[y] = nList[y+1]
                nList[y+1] = temp
        largestNum = (largestNum*10) + nList[listSize-1-x]
    return largestNum


size = int(input())
numList = [int(x) for x in input().split()]
print(formLargest(numList, size))


# Form the largest number with the array of single digits I/P {7,8,2,1,3} O/P 87321
#
# I/P {5,9,0,3,6,7,8,2,1} O/P 987653210
#
# Input Format
#
# Input will have array size and the values
#
# Constraints
#
# NIL
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 5
# 7 8 2 1 3
# Sample Output 0
#
# 87321