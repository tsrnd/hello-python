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
         return '';

    return carInfo
