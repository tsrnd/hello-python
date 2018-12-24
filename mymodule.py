def budle_sort(rdList) :
    for i in range(len(rdList)-2):
        j = len(rdList) -1 
        while (j > i):
            preIndex = j-1
            if rdList[j] < rdList[preIndex]:
                temp = rdList[j]
                rdList[j]= rdList[j-1]
                rdList[j-1] = temp
            j = j-1

import random
def randomList():
    a = []
    for i in range(10000):
        a.append(random.randint(-100000, 100000))
    return a