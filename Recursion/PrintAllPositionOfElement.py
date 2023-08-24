def printAllPosition(arr, n, i):
    if i == len(arr):
        return
    if arr[i] == n:
        print(i)
    printAllPosition(arr, n, i + 1)


print(printAllPosition([1, 4, 6, 4, 6, 1, 4, 1, 6, 6, 1, 4], 4, 0))
