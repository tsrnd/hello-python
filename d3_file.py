import os

def readData(filepath):
    check = True
    try:
        f = open(filepath)
        data = f.read()
    except:
        check = False
        print("has error during open file: {0}".format(filepath))
    finally:
        if check:
            f.close()
    return data


def create(data, filepath):
    check = True
    try:
        f = open(filepath, "x")
        f.write(data)
    except IOError as e:
        check = False
        print("has error during create new file: {0} with error: {1}".format(filepath, e.strerror))
    except:
        check = False
        print("has error during write file")
    finally:
        if check:
            f.close()

def overwrite(data, filepath):
    check = True
    try:
        f = open(filepath, "w")
        f.write(data)
    except:
        check = False
        print("has error during write file")
    finally:
        if check:
            f.close()

def append(data, filepath):
    check = True
    try:
        f = open(filepath, "a")
        f.write(data)
    except:
        check = False
        print("has error during write file")
    finally:
        if check:
            f.close()

def writeTo(data, filepath, mode):
    check = True
    try:
        f = open(filepath, mode)
        f.write(data)
    except:
        check = False
        print("has error during write file")
    finally:
        if check:
            f.close()

def delete(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print("The filepath {0} does not exist".format(filepath))
