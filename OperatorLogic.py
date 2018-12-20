print("Hello Operator With Logic")

a=1
b=2
c=3
d=5

# Operator Logic
print("Given a=",a,", b=",b,"When Logic a < b Then return",a<b )
print("Given a=",a,", b=",b,"When Logic a > b Then return",a>b)
print("Given a=",a,", b=",b,"When Logic a <= b Then return",a<=b)
print("Given a=",a,", b=",b,"When Logic a >= b Then return",a>=b)

# Operator Multi Logic

print("Given b=",b,", c=",c, ", d=" ,d,"When Logic b < c < d Then return",b<c<d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b < c > d Then return",b<c>d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b > c > d Then return",b>c>d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b > c < d Then return",b>c<d)

print("Given b=",b,", c=",c, ", d=" ,d,"When Logic b <= c <= d Then return",b<=c<=d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b <= c >= d Then return",b<=c>=d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b >= c >= d Then return",b>=c>=d)
print("Given b=",b,", c=",c,", d=" ,d,"When Logic b >= c <= d Then return",b>=c<=d)

#
parent="this is parent: Android, Ios"
android="Android"
ios="ios"
print("Given android=",android,", parent=",parent,", ios=",ios," When Check android in parent Then return ",android in parent)
print("Given android=",android,", parent=",parent,", ios=",ios," When Check ios in parent Then return ",ios in parent)
print("Given android=",android,", parent=",parent,", ios=",ios," When Check ios not in parent Then return ",ios in parent)

print("Good Bye")
