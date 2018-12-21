import re

def checkStr():
    txt = "qwertuyioasdflcxjzv"
    print(re.search("a",txt))
    print(re.findall("^1",txt))

checkStr()