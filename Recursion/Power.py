def power(number, pow):
    if pow == 0:
        return 1
    else:
        return number * power(number, pow - 1)


print(power(8, 3))