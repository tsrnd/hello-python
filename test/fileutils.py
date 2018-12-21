def readData(fileName='test.txt'):
    result = []
    f = open(fileName)
    line = f.readline()
    numb = 0
    while line:
        numb = float(line)
        result.append(numb)
        line = f.readline()
    f.close()
    print('File closed.')

    return result


def writeFile(data, fileName='test.txt'):

    try:
        with open(fileName, 'w') as files:
            for line in data:
                files.write(str(line))
                files.write('\n')
        files.close()
    except TypeError as err:
        print('Error:', err)
        return False

    print('File closed.')
    return True
