# Variables for String
name = "Void Ng"
print (name)

print ('If I input another name like Void Ng Fake')

name = "Void Ng"
name = "Void Ng Fake"
print (name)

# Variable for numbers

print ("******** Here is learn variables for numbers *****")

weight = 55
weight + 10 # Not count more

weight += 10 # is same not count more
weight2 = weight

print (weight)
print(weight2)

print ('another case')

original_num = 23
new_num = original_num + 7

num_to_be_added = 7

print (new_num)


print ("***** Finish learning variables for number ****")

# If statements

specices = "cat"

if specices == "cat":
    print("yep, it's cat.")

donut_condition = "fresh"
donut_price = "low"

if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0

print (buy_score)

x = 0
y =0
a = 1
b = 2 
c = 6
d = 7
g = 1
h = 2
e =4
f = 5
if (x == y or a == b) and c == d:
    g = h
else:
    e = f

# List of Python

cities =["atlanta","chicago","denver","los angeles","seattle"]

print("lấy phần tử trong mảng vd lấy phần tử thứ 3")

print (cities)
print (cities[3] + "la phan tu thu 3")

# thêm phần tử 
cities.append("da nang")
print (cities)
small_of_list_city = cities[2:5] # list used : tuples dùng ,
print (small_of_list_city)

task = ["call","meet","chat","smile"]
print ("task ban đầu", task)
del task[3]
print ("task sau khi xoá phần tử smile",task)

latest_task = task.pop(1)

print (latest_task)

# tuples in python
# Các element fixed còn lại tương tự như list

tasks_with_tuples = ("call", "meet", "see")

print (tasks_with_tuples)

# Getting info from user and converst Strings and number

# citi_to_check = input("Enter your name of city: ")

#print (citi_to_check)
