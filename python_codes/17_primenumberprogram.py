number = int(input("Enter a number: "))

for i in range(2, number +1):
    if number % i == 0:
        print("The number is not a prime number.")
        break
    else:
        print("The number is a prime number.")
        break
# is code me ham prime number check kar rahe hain. User se ek number input lete hain aur uske baad 2 se lekar us number tak ke numbers ke saath check karte hain ki kya wo number unme se kisi se divide hota hai ya nahi. Agar wo kisi se divide hota hai to wo prime number nahi hai, aur agar wo kisi se divide nahi hota hai to wo prime number hai.
