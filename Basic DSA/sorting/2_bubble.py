def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)
