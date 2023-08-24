import operator

def reversePolish(arr):
    stack = []
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    i = 0
    while i < len(arr):
        if arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
            first = stack.pop()
            second = stack.pop()
            result = ops[arr[i]](second, first)
            stack.append(result)
        else:
            stack.append(float(arr[i]))
        i += 1
    return stack[0]


print(reversePolish(['110', '50', '+', '4', '2', '5', '*', '-', '+', '10', '-', '40', '+']))
