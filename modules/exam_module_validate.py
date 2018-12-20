def checkLength(username):
    return 6 < len(username) < 32

def checkDigit(username):
    for i in range(0, len(username)):
        if username[i].isdigit(): return True;

    return False;
