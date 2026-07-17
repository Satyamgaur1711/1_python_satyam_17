list = [1, 2, 3, 4, 5]
for item in list:
    print(item)
else:
    print("Loop khatam ho gaya. and all items have been printed. Done!")
# yaha py for loop chalta rahega jabtak list ke sare items print nahi ho jate. For loop har item ko ek ek karke print karega. Jab list ke sare items print ho jayenge, to loop khatam ho jayega.


# break and continue statements in loops:
for i in range(0, 100):
    print(i)
    if i == 50:
        print("Loop khatam ho gaya, because i is equal to 50.")
        break
# yaha py for loop chalta rahega jabtak i ki value 50 nahi ho jati. Jab i ki value 50 ho jayegi, to loop khatam ho jayega, because of the break statement. Break statement loop ko turant khatam kar deta hai, chahe loop ke andar aur bhi statements hon.

for i in range(0, 10):
    if i == 5:
        print("Skipping the rest of the loop for i = 5.") # yaha py 5 hat jayega or waha py 5 print nahi hoga, because of the continue statement.
        continue
    print(i)
# yaha py for loop chalta rahega jabtak i ki value 10 nahi ho jati. Jab i ki value 5 ho jayegi, to loop us iteration ko skip kar dega, because of the continue statement. Continue statement loop ke us iteration ko skip kar deta hai, aur loop ke next iteration pe chala jata hai. Iska matlab hai ki jab i ki value 5 ho jayegi, to print(i) statement execute nahi hoga, aur loop ke next iteration pe chala jayega, jaha i ki value 6 ho jayegi


l = [1, 2, 3, 4, 5]
for item in l:
    pass # yaha py loop nahi chalega kyuke paas kuch bhi nahi karega, but loop ke andar pass statement hone ki wajah se loop khatam nahi hoga. Pass statement ek placeholder hai, jo ki loop ke andar likha jata hai, jab hume loop ke andar kuch bhi nahi karna hota hai. Iska matlab hai ki jab loop chalta hai, to pass statement execute hota hai, lekin uska koi effect nahi hota hai, aur loop ke next iteration pe chala jata hai.