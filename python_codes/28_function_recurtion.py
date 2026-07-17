# recurtion matlab apne function ko khud he call karna

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter a value jinka tum factorial chahty ho"))

print(f" the factorial of n in: {factorial(n)}" )
