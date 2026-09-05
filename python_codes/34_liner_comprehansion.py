a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

b = [] # even number wali
c = [] # odd number wali

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print(b) # even numbers
print(c) # odd numbers

# we can also do this using list comprehension in a single line of code...

x = [ i for i in a if i % 2 == 0] # even numbers
y = [ i for i in a if i % 2 != 0] # odd numbers

# list comprehension is a way to create lists in a single line of code.
# dict comprehension is a way to create dictionaries in a single line of code.
# set comprehension is a way to create sets in a single line of code.

print(x) # even numbers 
print(y) # odd numbers


dict = {i: i**2 for i in range(1, 11)} # dictionary comprehension
# haya dictionary comprehension ka example hai jisme humne 1 se 10 tak ke numbers ko keys banaya aur unke squares ko values banaya.
print(dict)

setss = {w**2 for w in range(1, 11)} # set comprehension
# haya set comprehension ka example hai jisme humne 1 se 10 tak ke numbers ko squares banaya aur unhe set me store kiya.
print(setss)
se = {"satyam", "kumar", "python", "programming", "language", "raj", "shukla"}
print(se)


# number ke ek hash value hoti hai jo ki uske memory address ko represent karti hai. Jab hum ek number ko set me store karte hain to uska hash value calculate hota hai aur uske basis par usko set me store kiya jata hai. Isliye set me duplicate values nahi hoti hain. set me number print karne ka sequence random and fix hota hai.

