def countOccurence(arr, n):
    if len(arr) == 0:
        return 0
    if arr[0] == n:
        return 1 + countOccurence(arr[1:], n)
    else:
        return countOccurence(arr[1:], n)


print(countOccurence([1, 1, 4, 1, 5, 5, 4, 1, 1, 1, 1], 1))
