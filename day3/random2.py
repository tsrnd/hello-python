import random


# random between 0.0 to 1.0 ( not include 1.0)
for i in range(10):
    x = random.random()
    print(x)



# random int ( including both )
x = random.randint(5, 10)
print(x)

# random choice
t = [1, 2, 3]
x = random.choice(t)
print(x)
