def isPalindrome(str):
    arr = list(str)
    if len(arr) == 0 or len(arr) == 1:
        return True
    if arr[0] != arr[len(arr) - 1]:
        return False
    return isPalindrome("".join(str[1:len(arr)-1]))


print(isPalindrome('abababab'))