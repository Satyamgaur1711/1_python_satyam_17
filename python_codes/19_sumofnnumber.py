# lets try some concept of sequence and series.
# sum of first n natural number = n(n+1)/2

n = int(input("Enter a number:  jiska tum sum of first n number nikalna chahte ho: "))
sum = 0
for i in range(n+1):
    sum = sum + i
print("The sum of first n natural numbers is:", sum)



# lets try to find the sum of first n even numbers.
# sum of first n even numbers = n(n+1)
neven = int(input("Enter a number:  tum kitne even number ka sum nikalna chahte ho: "))
sumeven = 0
for i in range(0, neven*2 +1 , 2):
    sumeven = sumeven + i
print("The sum of first", neven, "even numbers is:", sumeven)
