def partition(arr: list, start: int, end: int) -> int:
    pivot = start
    while start<end:
        while arr[start] <= arr[pivot]:
            start += 1
        while arr[end] > arr[pivot]:
            end -= 1
        if start<end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot] = arr[pivot], arr[end]
    return end


def quickSort(arr: list, start: int, end: int) -> None:
    if start<end:
        p = partition(arr, start, end)
        quickSort(arr, start, p-1)
        quickSort(arr, p+1, end)


arr = [ 9, 7, 8, 10, 1, 5 ]
quickSort(arr, 0, len(arr)-1)
print(arr)
