# def replaceFirstDigitRegExp(input):
#     for i in range(0, len(input)):
#         if input[i].isdigit():
#             return input[:i] + "#" + input[i + 1:]
#             print("aphu",input[:i])
# print(replaceFirstDigitRegExp("123, 8 phutrna"))



def replaceFirstDigitRegExp(input):
    for i, c in enumerate(input):
        print("in c",c)
        print("in i",i)
        # print(ord(c))
        if ord(c) >= 48 and ord(c) <= 57:
            print(ord(c))
            return input[0:i] + '#'+ input[i+1:] 
print(replaceFirstDigitRegExp("aaaa3sssss"))


# presidents = ["Washington"]
# for num, name in enumerate(presidents):
#     print(num)
#     # print("President {}: {}".format(num, name))