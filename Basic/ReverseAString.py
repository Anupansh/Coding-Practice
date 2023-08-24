def usingStack(line):
    stack = []
    reversedString = ""
    for i in line:
        stack.append(i)
    for i in range(len(line)):
        reversedString += stack.pop()
    return reversedString

def usingSwap(line):
    list1 = list(line)
    i = 0
    n = len(list1)
    while i<n/2:
        temp = list1[i]
        list1[i] = list1[n-1-i]
        list1[n-1-i] = temp
        i+=1

    return ''.join(list1)

print(usingStack("kcatS gnisu olleH fo esreveR"))
print(usingSwap("pawS gnisu olleH fo esreveR"))