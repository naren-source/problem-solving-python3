def checkNextLargest(nList: list, size: int) -> None:
    for main in range(size):
        diff = -1
        nextGreat = nList[main]
        for sub in range(size):
            if nList[sub] > nList[main] and \
                    (nList[sub] - nList[main] < diff or diff == -1):
                diff = nList[sub] - nList[main]
                nextGreat = nList[sub]
        if diff == -1:
            print(f"{nList[main]}->")
        else:
            print(f"{nList[main]}->{nextGreat}")


lSize = int(input())
nList = [int(x) for x in input().split()]
checkNextLargest(nList, lSize)


# Write a program to print the next larger element for every element in the given array.
#
# Input Format
#
# size of the array and the elements
#
# Constraints
#
# NIL
#
# Output Format
#
# element -> larger element
#
# Sample Input 0
#
# 7
# 1 9 7 4 2 6 8
# Sample Output 0
#
# 1->2
# 9->
# 7->8
# 4->6
# 2->4
# 6->7
# 8->9
