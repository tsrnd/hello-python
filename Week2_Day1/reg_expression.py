import re
str = "Tôi la Đặng Ngọc Vũ"

matchObj = re.match(r'(.*) la (.*?) .*', str, re.M | re.I)

if matchObj:
    print("mathObj.group: ", matchObj.group(0))
else:
    print("Khong có kết nối")

searchObj = re.search(r'(.*) la (.*?) .*', str, re.M | re.I)

if matchObj:
    print("searchObj.group: ", searchObj.group())
else:
    print("Khong tìm thấy")

line = "Hoc Python la de hon hoc Java?"

matchObj = re.match(r'la', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("Khong co ket noi!!")

searchObj = re.search(r'la', line, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Khong tim thay!!")

replaceObj = re.sub(r'la', "là", str)

print(replaceObj)
