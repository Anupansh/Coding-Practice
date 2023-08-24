def multiplication(m,n):

    if n == 0:
        return 0

    return m + multiplication(m, n-1)

print(multiplication(4,3))