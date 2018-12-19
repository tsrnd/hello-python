dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8
dict['School'] = "DPS School"
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print("item ",dict.items())

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))
dict = dict.fromkeys(seq, "Ali")
print ("New Dictionary : %s" %  str(dict))

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'female' }

dict.update(dict2)
print ("updated dict : ", dict)
