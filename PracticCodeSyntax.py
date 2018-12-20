def allLongestStrings(inputArray):
    max = len(inputArray[0])
    result = []
    for element in inputArray:
        if len(element) >= max:
            max = len(element)
    for element in inputArray:
        if len(element) == max:
            result.append(element)
    return result

# print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))


def commonCharacterCount(s1, s2):
    count = 0
    if(len(s1) < len(s2)):
        s1, s2 = list(s2), list(s1)
    else:
        s1, s2 = list(s1), list(s2)
    for element in s1:
        if element in s2:
            count = count+1
            del s2[s2.index(element)]
            print(s2)
    return count


# print(commonCharacterCount("abca", "xyzbac"))

def isLucky(n):
    n = str(n)
    count = 0
    for i, ii in zip(n, n[int(len(n)/2):]):
        count = count + int(i)-int(ii)
    if(count == 0):
        return True
    else:
        return False


# print(isLucky(1230))

def sortByHeight(a):
    result = []
    notTree = []
    for element in a:
        if element != -1:
            notTree.append(element)
    for element in a:
        if element == -1:
            result.append(element)
        else:
            result.append(min(notTree))
            del notTree[notTree.index(min(notTree))]
    return result


def sortByHeight2(a):
    result = []
    notTree = [elem for elem in a if elem != -1]
    notTree.sort()
    notTree.reverse()
    for element in a:
        if element == -1:
            result.append(element)
        else:
            result.append(notTree.pop())
    return result

# print(sortByHeight2([-1, 150, 190, 170, -1, -1, 160, 180]))


def reverseParentheses(s):
    count = s.count("(")
    while(count > 0):
        s = s.replace(s[s.rfind("("):s.find(")")+1],
                      s[s.rfind("(")+1:s.find(")")][::-1])
        count = count - 1
    return s


# print(reverseParentheses("abc(cba)ab(bac)c"))

