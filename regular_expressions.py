import re

s = "Today 1 is 2 beautiful 33333 day 4 . If you want 2 go out with nhatnguyen30041995@gmail.com.vn"
# \d get number
number = re.findall(r'\d{1,3}',s)
print(number)
# \w get a word
word = re.findall(r'[a-zA-Z]\w{4,}',s)
print(word)
# get email
email = re.findall(r'[a-zA-Z]\w{3,}@[a-zA-Z]\w{3,}.[a-zA-Z]\w{2,}',s)
email = re.findall(r'[a-zA-Z]\w{3,}@[a-zA-Z]\w{3,}.[a-zA-Z.]{2,}',s)
print(email)

s = '''
Today 1 is 2 beautiful "33333 day 4" . If you want 2 go out with 'nhatnguyen30041995@gmail.com.vn'
'''
result = re.findall(r'"(.*?)"',s)+re.findall(r"'(.*?)'",s)
print(result)