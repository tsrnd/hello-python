def sameDigitNumber(n):
    s = str(n)
    print("phantu0", s[0])
    return s.replace(s[0], '') == ''
print(sameDigitNumber(111112))