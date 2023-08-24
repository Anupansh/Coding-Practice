def countDigit(n):
    if n // 10 == 0:
        return 1

    return 1 + countDigit(n//10)

print(countDigit(923456))
