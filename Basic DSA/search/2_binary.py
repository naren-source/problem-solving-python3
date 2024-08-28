def binarySearch(arrList: list, key: int) -> int:
    return binarySearchUtil(arrList, 0, len(arrList)-1, key)

def binarySearchUtil(arr, start, end, key):
    if start>end:
        return -1
    middle = int((start + end) / 2)
    if key < arr[middle]:
        return binarySearchUtil(arr, start, middle-1, key)
    elif key > arr[middle]:
        return binarySearchUtil(arr, middle+1, end, key)
    else:
        return middle

arr = [ 2, 3, 4, 10, 40 ]
print(binarySearch(arr, 2))
print(binarySearch(arr, 3))
print(binarySearch(arr, 4))
print(binarySearch(arr, 10))
print(binarySearch(arr, 40))
print(binarySearch(arr, 0))
print(binarySearch(arr, -1))
print(binarySearch(arr, 50))
