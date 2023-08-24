def geometricSum(n):

    if n == 0:
        return 1

    smallAns = geometricSum(n-1)

    return smallAns +( 1 / pow(2,n))

print(geometricSum(3))