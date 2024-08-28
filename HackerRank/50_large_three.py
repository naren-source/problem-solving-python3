def largestThree(numList: list, size: int) -> None:
    largeThree = {
        "one": numList[0],
        "two": numList[0],
        "three": numList[0]
    }
    for x in numList:
        if x > largeThree["three"]:
            if x > largeThree["two"]:
                if x > largeThree["one"]:
                    largeThree["three"] = largeThree["two"]
                    largeThree["two"] = largeThree["one"]
                    largeThree["one"] = x
                else:
                    largeThree["three"] = largeThree["two"]
                    largeThree["two"] = x
            else:
                largeThree["three"] = x
    print(f"{largeThree['one']}, {largeThree['two']}, {largeThree['three']}")


listSize = int(input())
nList = [int(x) for x in input().split()]
largestThree(nList, listSize)


# Given an array with all distinct elements, find the largest three elements.
#
# Input Format
#
# Input contains the no of elements & array values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the largest elements
#
# Sample Input 0
#
# 6
# 10 4 3 50 23 90
# Sample Output 0
#
# 90, 50, 23
