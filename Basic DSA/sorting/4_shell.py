def shellSort(arr):
    length = len(arr)
    gap = int(length/2)
    while gap > 0:
        for i in range(gap, length):

            j = i
            temp = arr[j]
            while j>=gap and arr[j] < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp

        gap //= 2

arr = [23, 45, 12, 67, 34, 89, 90, 11, 50, 99]
shellSort(arr)
print(arr)
