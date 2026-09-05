name = ["satyam", "raj", "rajit", "aman", "akshay", "sachin", "piyush"]

for i in name:
    print(len(i))

length = list(map(len, name))
print(length)

temp = [15.45 , 45.56, 465.55, 23.3, 2343.23, 40]

def c2f (x):
    return (x*9/5) + 32

farenhight = list(map(c2f, temp))
print(farenhight)

farhight = list(map(lambda x: (x*9/5) + 35, temp))
print(farhight)

mark = [15, 54, 74, 64, 94, 37, 62]

passed = list(filter(lambda x: x>= 40, mark))
print(passed)


result = dict(zip(name, mark))
result2 = list(zip(name, mark))

print(result2)
# jisme sabse lovest value hai waha tak marz ho jayega.
print(result)

