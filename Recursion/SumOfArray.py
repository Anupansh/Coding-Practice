def sumOfArray(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sumOfArray(arr[1:])

print(sumOfArray([1,2,3,4,5,6]))