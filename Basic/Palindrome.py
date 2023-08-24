def canDeleteOneChar(text):  # Checking if removing one char can make it palindrome or not
    arr = list(text)
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start].upper() != arr[end].upper():
            if  not(validPalindrome("".join(arr[start:end])) or validPalindrome("".join(arr[start + 1:end + 1]))):
                print(arr[start + 1:end + 1])
                print("".join(arr[start:end]))
                print("".join(arr[start:end - 1]))
                return "Isse naa ho paayega"
        start += 1
        end -= 1
    return "Ho Jaayega"


def validPalindrome(text):  # Checking for whether Palindrome or not
    arr = list(text)
    j = 0
    while j < len(arr) / 2:
        if arr[j].upper() != arr[len(arr) - (j + 1)].upper():
            return bool(0)
        j += 1
    return bool(1)


print(validPalindrome("abababac"))
print(canDeleteOneChar("dabababacd"))
