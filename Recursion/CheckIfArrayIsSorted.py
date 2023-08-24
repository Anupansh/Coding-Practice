def isArraySorted(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False

    return isArraySorted(arr[1:])


print(isArraySorted([1, 2, 3, 4, 5, 6, 3]))
