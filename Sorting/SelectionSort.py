# Sorting in which first element is taken and the rest of array is searched for the smallest number.
# If there is one swap the positions of first and that element and move i from first element to next element

def selectionSort(arr):
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
        i += 1
    print(arr)


selectionSort([33, 56, 44, 42, 60, 21, 7, 34, 81, 47])
