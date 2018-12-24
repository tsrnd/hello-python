def budle_sort(rdList) :
    for i in range(len(rdList)-2):
        j = len(rdList) -1 
        while (j > i):
            if rdList[j] < rdList[j-1]:
                temp = rdList[j]
                rdList[j] = rdList[j-1]
                rdList[j-1] = temp
            j -=1

def gnome_sort(rdList) :
    pos = 0
    while pos < len(rdList):
        if pos == 0 or rdList[pos] >= rdList[pos - 1]:
            pos += 1
        else :
            temp = rdList[pos]
            rdList[pos] = rdList[pos-1]
            rdList[pos-1] = temp
            pos -= 1

import random
def randomList():
    a = []
    for i in range(10000):
        a.append(random.randint(-100000, 100000))
    return a
