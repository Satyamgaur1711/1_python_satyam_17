# howme world conditio
a = int(input("Enter number one"))
b = int(input("Enter number two"))
c = int(input("Enter number three"))
d = int(input("Enter number four"))

if a > b:
    x = a
else:
    x = b
# print(x)

if c > d:
    y = c
else:
    y = d
# print(y)

if x>y:
    print(x)
else:
    print(y)

# new method to solve it.

if(a>b and a>c and a > d):
    print("gretest number is a ", a)

elif(b>a and b>c and b > d):
    print("gretest number is b ", b)

elif(c>b and c>a and c > d):
    print("gretest number is c ", c)

else:
    print("grtest number is d" , d)
