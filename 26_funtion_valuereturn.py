def avg():
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    c = int(input("enter another number"))

    average = (a + b + c) / 3
    print("the average is", average)
    return average


returnvalue = avg()

print(returnvalue)
print(type(returnvalue)) # string agar return me koi string hai to nahi to flot value hoga.

# yaha py return value jo hai returnvalue wale variable ko asign hogi.

