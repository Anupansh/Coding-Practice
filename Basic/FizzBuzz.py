# Multiple of 3 - Print Fizz
# Multiple of 5 - Print Buzz
# Multiple of 3 and 5 - Print FizzBuzz

def fizBuzz(n):
    ans = list()
    j = 1
    while j <= n:
        if j % 3 == 0 and j % 5 == 0:
            ans.append('FizzBuzz')
        elif j % 5 == 0:
            ans.append('Buzz')
        elif j % 3 == 0:
            ans.append('Fizz')
        else:
            ans.append(j)
        j += 1
    return ans


print(fizBuzz(16))
