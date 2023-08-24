def countZeros(n):

    if n == 0:
        return 0

    smallAns = countZeros(n//10)

    if n % 10 == 0:
        return smallAns + 1
    else:
        return smallAns

print(countZeros(104))