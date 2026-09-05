# decorator is a function which takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper



@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # this will call the wrapper function which will call the say_hello function and print the messages before and after the function is called.