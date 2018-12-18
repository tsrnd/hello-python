# multiple assignment
a = b = c = 1
print("a =", a, ", b = ", b, ", c = ", c)

a, b, c = 1, 2, "minh"
print("a =", a, ", b = ", b, ", c = ", c)

# string
str = "Hello world!"
print(str)
print(str[1])
print(str[2:5])
print(str[2:])
print(str*2)
print(str[-1])
print(str[:-1])
print(str+"concatenate")

# list
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_1)
list_2 = ["a", "b", "c", 18, 8, 95, True, (18, 8, 95)]
print(list_2)
print(list_2[-1])
print(list_1[2:5])  # from index 2 to before 5
print(list_1[2:])  # from index 2 -> end
print(list_1[-5:])  # from index -5 -> end
print(list_1[:-5])  # from start -> before -5
print(list_1[2::3])  # jump 3 from index 2
print(list_1[::-1])  # revert list

list_1.append(10)
print(list_1)
