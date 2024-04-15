def checkLargestSubarray(nList: list, size) -> None:
    left, right = -1, -1
    for x in range(size-1):
        flag = 0
        if nList[x] == 1:
            flag += 1
        else:
            flag -= 1
        for y in range(x+1, size):
            if nList[y] == 1:
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                if (y - x) > (right - left):
                    left = x
                    right = y
    if left == right:
        print("No such array")
    else:
        print(f"{left}->{right}")


listSize = int(input())
nList = [int(x) for x in input().split()]
checkLargestSubarray(nList, listSize)
