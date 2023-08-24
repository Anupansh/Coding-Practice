def longestCommonPrefix(strs):
    emptyString = ''
    first = strs[0]
    i = 0
    while i < len(first):
        j = 1
        while j < len(strs):
            if i == len(strs[j]) or first[i] != strs[j][i]:
                return emptyString
            j += 1
        emptyString += first[i]
        i += 1
    return emptyString


print(longestCommonPrefix(['Hello', 'Hellova', 'Hellotta', 'Hellow']))
