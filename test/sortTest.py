import random
import fileutils


def initData_Increment():
    """
        Method generate 10k number increment.
    """
    dataArr = []
    for i in range(1, 10001):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'increment.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_Decrement():
    """
        Method generate 10k number decrement.
    """
    dataArr = []
    for i in range(1000, 1, -1):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'decrement.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_Random():
    """
        Method generate random 10k number.
    """
    dataArr = []
    for i in range(1, 10001):
        dataArr.append(random.uniform(1, 10001))

    if fileutils.writeFile(dataArr, 'random.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomFirst():
    """
        Method generate 10k number with 2k first random and 8k last are increment values.
    """
    return


def initData_RandomMid():
    """
        Method generate 10k number with 2k first increment, 2k last increment and 4k at mid are random values.
    """
    return


def initData_RandomLast():
    """
        Method generate 10k number with 2k first increment values and 2k last are random.
    """
    return


def initData_RandomFirstDesc():
    """
        Method generate 10k number with 2k first random and 8k last are decrement values.
    """
    return


def initData_RandomMidDesc():
    """
        Method generate 10k number with 2k first decrement, 2k last decrement and 4k at mid are random values.
    """
    return


def initData_RandomLast():
    """
        Method generate 10k number with 2k first decrement values and 2k last are random.
    """
    return


initData_Increment()
initData_Decrement()
initData_Random()