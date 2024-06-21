def selectionSort(arr):
    length = len(arr)
    for i in range(0, length):
        minimum = i

        for j in range(i+1, length):
            if arr[j] < arr[minimum]:
                minimum = j

        temp = arr[minimum]
        arr[minimum] =  arr[i]
        arr[i] = temp

arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print(arr)
