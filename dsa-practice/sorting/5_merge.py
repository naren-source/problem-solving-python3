def mergeSort(arr):
    length = len(arr)
    if length < 2:
        return
    middle = int(length / 2)
    left = arr[:middle]
    right = arr[middle:]
    mergeSort(left)
    mergeSort(right)

    l = r = m = 0
    while l< len(left) and r < len(right):
        if left[l] < right[r]:
            arr[m] = left[l]
            l+=1
        else:
            arr[m] = right[r]
            r+=1
        m+=1

    while l < len(left):
        arr[m] = left[l]
        l += 1
        m += 1

    while r < len(right):
        arr[m] = right[r]
        r += 1
        m += 1

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)
