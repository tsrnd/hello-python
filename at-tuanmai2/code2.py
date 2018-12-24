def replaceFirstDigitRegExp(input):
    for i in range(0, len(input)):
        if input[i].isdigit():
            return input[:i] + "#" + input[i + 1:]

def countIncreasingSequences(n, k):
    tong = 0
    if n > k:
        return 0
    elif n == k:
        return 1
    else:
        so = k - n + 1
        for i in range(0, k - n + 1):
            tong = tong + so
            so -= 1
        return tong

def middleName(firstName, lastName, para):
    kqs = []
    firstName1 = firstName.replace(' ', '`')
    lastName1 = lastName.replace(' ', '`')
    para = para.replace(firstName, firstName1).replace(lastName, lastName1).replace(' ', '')
    firstName = firstName1
    lastName = lastName1
    while len(para) > 0:
        print('para = ' + para)
        try:
            index1 = para.index(firstName)
        except Exception:
            break
        para = para[index1:]
        lp = para[len(firstName) + 1:]
        try:
            index2 = lp.index(lastName) + len(firstName) + 1
            print(index2)
        except Exception:
            break
        kq = para[len(firstName):index2].replace('`', ' ').strip()
        print('kq = ' + kq)
        para = para[1:]
        if kq.istitle():
            if kq.find(' ') == -1:
                kqs.append(kq)
        print(kqs)
    

    return kqs

#print(middleName('Jan', 'Levinson', 'Jan Jan Jan Jan Jan Jan Levinson Levinson Levinson Levinson Levinson'))
def slowLeak(distance, initialTimePerKm, timeIncreasePerKm, timeToRefill):
    return distance and initialTimePerKm * distance - timeToRefill + min(c * timeToRefill + distance // c * (distance - c + distance % c) // 2 * timeIncreasePerKm for c in range(1, distance + 1))

print(slowLeak(5,10,5,20))1