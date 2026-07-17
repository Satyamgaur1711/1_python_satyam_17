def multiplication_table(n):
    for i in range(1, 11): 
        print(f"{n} x {i} = {n * i}")

# Example usage:
number = int(input("Enter a number to see its multiplication table: "))

print(multiplication_table(number))

