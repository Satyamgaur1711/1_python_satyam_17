# list uning py.p

list = [1546, "satyam", 3465, "shiva", 512]
print(list)

i = 0
while i < len(list):
    print(list[i])
    i = i + 1
print("if you want to add more elements to the list.")
a = input("enter you next string element: ")
list.append(a)
print(list)


