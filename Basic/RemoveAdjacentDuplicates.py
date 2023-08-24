from collections import deque

def removeAdjacentDuplicates(str):
    arr = list(str)
    emptyString = ''
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            i += 2
            if i == len(str) - 1:
                emptyString += arr[i]
        else:
            emptyString += arr[i]
            i += 1
            if i == len(str) - 1:
                emptyString += arr[i]
    return emptyString

#print(removeAdjacentDuplicates('aaabccdeefghuuij'))

def removeDuplicateUsingStack(str):
    stack = deque()
    arr = list(str)
    i = 0
    while i < len(arr):
        if not(stack):
            stack.append(arr[i])
        elif arr[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(arr[i])
        i += 1

    return  ''.join(stack)

print(removeDuplicateUsingStack('Mississippi'))
