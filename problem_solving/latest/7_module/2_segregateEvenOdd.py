def evenOddSegregation(numList: list) -> None:
    left = -1
    right = -1
    for idx, val in enumerate(numList):
        if numList[idx] %2 == 0:
            left = idx
        elif numList[idx] %2 == 1 and right == -1:
            right = idx
        if left > right and (left > -1 and right > -1):
            temp = numList[right]
            numList[right] = numList[left]
            numList[left] = temp
            left = right
            right += 1


def rearrangeEvenAndOdd(arr, n):
    j = -1
    for i in range(0, n):
        if arr[i] % 2 == 0:
            j = j + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


listSize = int(input())
nList = [int(x) for x in input().split()]
# evenOddSegregation(nList)
rearrangeEvenAndOdd(nList, listSize)

for x in nList:
    print(x, end=" ")


