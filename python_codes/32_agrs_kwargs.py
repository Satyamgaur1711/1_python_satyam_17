# args and kwargs in python are use take multiple arguments in a function. args is used to take multiple positional arguments and kwargs is used to take multiple keyword arguments....

def addition(*number_tuple):
    sum = 0
    for i in number_tuple:
        sum += i
    return sum

x = addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x)

def details(**kwargs):

    return kwargs


y = details(name="Satyam", age=20, city="azamgarh", country="India", state="U.P", pincode=223223, phone=1234567890, email="satyam@example.com")

print(y)

