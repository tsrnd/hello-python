import re
regu1 = re.compile('\d')
print(regu1.findall("My name is Thai, I'm 22 years old, I was born in 1996"))
rege2 = re.compile('\d+')
print(rege2.findall("My name is Thai, I'm 22 years old, I was born in 1996"))

regu3 = re.compile('ab*')
print(regu3.findall("ababbaabbb"))

print(re.split('\W+', "My name is thai, I'm 22 years old"))
print(re.split('\d+', "This year is 2018, and I'm 22 years old"))
print(re.split('\d+', "On 12th Jan 2016", 1))
print(re.split('[a-f]+', "Aey, Boy oh boy, come here", flags=re.IGNORECASE))
