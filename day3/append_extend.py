List = []
print("Inital blank List: ")
print(List)

List.append(1)
List.append(2)
List.append(4)
print('\nList after Addition of Three elements: ')
print(List)

for i in range(1,4):
    List.append(i)

print("\nList after Addition of elements from 1-3: ") 
print(List)

List.append((5, 6))
print("\nList after Addition of a Tuple: ") 
print(List)

List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 


List.insert(3, 12) 
List2.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List)

List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List)
