import datetime
# Display string to screen.
print("Hello world!")

# operator
print("Sum of two number (5, 6) are :", 5+6)
print("Sub of two number (5, 6) are :", 5-6)
print("Multiply of two number (5, 6) are :", 5*6)
print("Devine of two number (5, 6) are :", 5/6)

#Check if statement
print("Check person(16) are adult or child.")
if 16 < 18:
    print("16 age are adult")
else:
    print("you are adult")

#Check multy choice statement.
curDate = datetime.date.today().weekday()
if curDate == 0:
    print("Today are Monday")
elif curDate == 1:
    print("Today are Tuesday")
elif curDate == 2:
    print("Today are Wednesday")
elif curDate == 3:
    print("Today are Thusday")
elif curDate == 4:
    print("Today are Friday")
elif curDate == 5:
    print("Today are Saturday")
else:
    print("Today are Sunday")

