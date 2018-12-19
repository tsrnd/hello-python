name = "Quoc Nguyen P"
age = 25
height = 164.5

print (name + " age: " +str(age) + "height: " +str(height))

# Python List

me = [ 'Quoc Nguyen P', 25 , 'Da Nang City']
company = ['Asiantech', 'android team']

print (me)
print (me[0])
print (me[1:2])
print (me + company)

# Python Tuples

remember = """
Python tuples
1. Nó là kiểu dữ liệu dùng lưu trữ các đối tượng không đổi về sau giống như hằng số.
2. Lưu ý có thể dùng dấu ngoặc () hoăc không nhưng khuyên nên dùng.

# Truy cập
 - 0 từ trái -> phải và -1 phải  -> trái
"""
print (remember)

dayOfWeek = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
month = ('jan', 'feb', 'mar', 'apr', dayOfWeek)

print ('l-r: ' + dayOfWeek[0])
print ('r-l: ' + dayOfWeek[-1])

print ('tuple lồng nhau: ' + str(month))

# Dictionary

contentOfDictionary = """
Dictionary trong py:
    - Là một cặp key value không thứ tự. tương tự như Json 
    - Là container chứa dữ liệu.

# Một vài phương thức có sẵn:
    cmd(dict1, dict2) -> so sanh
    len(dict) => số item của dict
    dict.items() => trả về tất cả cặp key-value của dict hoặc có thể gọi dict.keys() => trả về tất cả key của dict
    ...

"""

print (contentOfDictionary)

employ = {'ten': 'at-quocnguyen', 'MNV': 158,  'at-tuanma': 50, 'jop': 'android derverloper'}
employ1 = {'tem': 'at_tuanma', 'MNV': 50, 'job': 'IOS deverloper'}


print (employ)
print (employ1)

print ('truy cập giá trị: Mã nhân viên của employ là: ' + str(employ['MNV']))