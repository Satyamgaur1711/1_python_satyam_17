# dunder methods are special methods in python that have double underscores at the beginning and end of their names. They are also known as magic methods or special methods. Dunder methods allow you to define how objects of a class behave with respect to built-in operations, such as addition, subtraction, string representation, and more. we don't need to call them directly, they are called automatically by python when we use built-in operations on objects of a class.

class book:
    def __init__(self, name , page):
        self.name = name
        self.page = page


    def __str__(self):
        return f"book name is {self.name} and page is {self.page}"  # this method is used to return the string representation of the object. it is called when we use print() function on the object.

    def __add__(self, other_book):
        return self.page + other_book.page  # this method is used to add two objects of the class. it is called when we use + operator on the objects of the class.

obj1 = book("python_book", 100)
obj2 = book("java_book", 200)

print(obj1)  # this will call the __str__() method of the class book and return the string representation of the object obj1.
print(obj2)


print(obj1 + obj2)  # this will call the __add__() method of the class book and return the sum of the pages of the two objects obj1 and obj2.
