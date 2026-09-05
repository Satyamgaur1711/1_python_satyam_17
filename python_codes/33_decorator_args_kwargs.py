

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print(result)
        print("Something is happening after the function is called.")
        return result
    return wrapper


# this decorator can be used to decorate any function which takes any number of positional and keyword arguments... 


@my_decorator
def addition(*number_tuple):
    sum = 0
    for i in number_tuple:
        sum += i
    return sum

x = addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x) # wo value print hogi jo function return kar rahi hai...

