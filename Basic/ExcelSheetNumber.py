# Like in an Excel sheet if input is A print 1, If AA print 27 etc

def excelSheetNumber(var):
    ans = 0
    j = 0
    size = len(var)
    while j < size:
        ans = ans + pow(26, size - (j + 1)) * (ord(var[j]) - 64)
        j += 1
    return ans


print(excelSheetNumber("BA"))
