def swapList(numList: list, size: int) -> list:
    newList: list = [-1] * size
    for idx, val in enumerate(numList):
        newList[val] = idx
    return newList


#diff prob but similar
def swapList1(arr: list, n: int) -> list:
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n

    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)

    return arr


listSize = int(input())
nList = [int(x) for x in input().split()]
nList = swapList(nList, listSize)
for x in nList:
    print(x, end=" ")
