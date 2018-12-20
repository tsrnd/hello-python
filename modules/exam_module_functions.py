import exam_module_validate as validate


def checkUser(username):
    # Validate length
    if validate.checkLength(username) == False:
        return False
    if validate.checkDigit(username) == True:
        return False

    # Maybe check Japan character.
    return True


def getCarInfoByName(carName):
    cars = {
        'turbo': 'turbo canel',
        'kia': 'KIA morning',
        'mec': 'Mecedes'
    }

    try:
        carInfo = cars[carName]
    except KeyError:
        return ''

    return carInfo


def readAndDisplay(fileName = 'test.txt'):
    f = open(fileName)
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
    return


def writeFile(fileName = 'test.txt'):
    print('please input content: ')
    fileContent = []
    while True:
        inp = input()
        if len(inp) == 0 or inp == '\n':
            break
        else:
            fileContent.append(inp)
            inp = ''

    with open(fileName, 'w') as the_file:
        for line in fileContent:
            the_file.write(line)
            the_file.write('\n')
    the_file.close()
    print('File closed.')
    return
