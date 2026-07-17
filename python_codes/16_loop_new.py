# my name is satyam gaur and i am learning python programming language. with the help of code with harry youtube channel.

a = 1
while a<31:
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
    a = a + 1


list = ["satyam", "raj", "shiva", "piyush"]
for k in list:
    print(k)
newname = input("enter the new name: ")
list.append(newname)
for k in list:
    print(k)


namlist = ["satyam", "raj", "shiva", "piyush",  "harry", "rohan", "mohit", "sanjana", "suman", "satyarth"]
for name in namlist:
    if name.startswith("s"):
        print(f"{name} happy birthday {name}")
