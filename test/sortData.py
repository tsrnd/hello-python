import random
import fileutils


def initData_Increment():
    """
        Method generate 10k number increment.
    """
    dataArr = []
    for i in range(1, 10001):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'data_increment.txt'):
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

    if fileutils.writeFile(dataArr, 'data_decrement.txt'):
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

    if fileutils.writeFile(dataArr, 'data_random.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomFirst():
    """
        Method generate 10k number with 2k first random and 8k last are increment values.
    """
    dataArr = []
    for i in range(1, 2001):
        dataArr.append(random.uniform(1, 10001))

    for i in range(2001, 10001):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'data_randomFirst.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomMid():
    """
        Method generate 10k number with 2k first increment, 2k last increment and 6k at mid are random values.
    """
    dataArr = []
    for i in range(1, 2001):
        dataArr.append(random.uniform(i, i+1))

    for i in range(2001, 8001):
        dataArr.append(random.uniform(1, 10001))

    for i in range(8001, 10001):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'data_randomMid.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomLast():
    """
        Method generate 10k number with 8k first increment values and 2k last are random.
    """
    dataArr = []
    for i in range(1, 8001):
        dataArr.append(random.uniform(i, i+1))

    for i in range(8001, 10001):
        dataArr.append(random.uniform(1, 10001))

    if fileutils.writeFile(dataArr, 'data_randomLast.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomFirstDesc():
    """
        Method generate 10k number with 2k first random and 8k last are decrement values.
    """
    dataArr = []
    for i in range(1, 2001):
        dataArr.append(random.uniform(1, 10001))

    for i in range(10001, 2001, -1):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'data_randomFirstDesc.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomMidDesc():
    """
        Method generate 10k number with 2k first decrement, 2k last decrement and 4k at mid are random values.
    """
    dataArr = []
    for i in range(10001, 8001, -1):
        dataArr.append(random.uniform(i, i+1))

    for i in range(8001, 2001, -1):
        dataArr.append(random.uniform(1, 10001))

    for i in range(2001, 1, -1):
        dataArr.append(random.uniform(i, i+1))

    if fileutils.writeFile(dataArr, 'data_randomMidDesc.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def initData_RandomLastDesc():
    """
        Method generate 10k number with 8k first decrement values and 2k last are random.
    """
    dataArr = []
    for i in range(10001, 2001, -1):
        dataArr.append(random.uniform(i, i+1))

    for i in range(2001, 1, -1):
        dataArr.append(random.uniform(1, 10001))

    if fileutils.writeFile(dataArr, 'data_randomLastDesc.txt'):
        print('Write data successful!')
    else:
        print('Create data fail.')
    return


def createDatafiles():
    initData_Increment()
    initData_Decrement()
    initData_Random()
    initData_RandomFirst()
    initData_RandomMid()
    initData_RandomLast()
    initData_RandomFirstDesc()
    initData_RandomMidDesc()
    initData_RandomLastDesc()

