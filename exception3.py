try:
  f = open("hello-python/text.txt", "w")
  f.write("Lorum Ipssum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
w
#   f = open("hello-python/text.txt", "r")
# # print(f.read())
# # print(f.read())
# # f.close
# print(f.readline())
# for x in f:
#     print(x)
# f = open("hello-python/text.txt", "w")
# f.write("Woops! I have deleted the content!")