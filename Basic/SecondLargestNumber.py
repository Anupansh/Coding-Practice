def secondLargestNo(arr):
    largest = arr[0]
    second = 0
    i = 1
    while i < len(arr):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second:
            second = arr[i]
        i += 1

    return second

print(secondLargestNo([23,16,29,3,94,96,8,22,49]))
