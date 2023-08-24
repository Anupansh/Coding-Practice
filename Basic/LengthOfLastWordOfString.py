def lastWordLength(line):
    count = 0
    n = len(line)
    i = 0
    while i < n:
        if line[i] != " ":
            count += 1
            i += 1
        else:
            while i < n and line[i] == " ": i += 1
            if i == n:
                return count
            else:
                count = 0
    return count


print(lastWordLength("       Heyaaaa      there  "))
