def isElementPresent(arr, n):
    if len(arr) == 0:
        return False
    if arr[0] == n:
        return True

    return isElementPresent(arr[1:], n)


print(isElementPresent([1, 2, 3, 4, 5, 6], 6))
