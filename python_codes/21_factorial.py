# lets find factorial of a number using python
number = int(input("Enter a number to find its factorial: "))
i = 1
factorial = 1
while i <= number:
  factorial = factorial * i
  i = i + 1
  print(f"the factorial equals to {factorial}")
