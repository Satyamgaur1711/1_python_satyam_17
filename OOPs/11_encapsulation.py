print("hallo, now i am using git for my code bas")

class animal:
    a = 12
    string = "hallo, this is string in class animal"
    def __init__(self, name, age):
        self.name = name 
        self.age = age


obj1 = animal("dog", 5)
obj1.a = 10

print(obj1.a)
# hear and object have power to change the method and variable of class. but if we want to protect the method and variable of class then we use encapsulation.



class factory():
    __name = "satyam_gaur_factory"
    __location = "delhi"  # hear we use double underscore to make the variable private and protect it from outside the class.
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

obj2 = factory("car", 1000)

obj2.__name = "new_factory"  # hear we try to change the private variable of class but it will not change because it is private variable.
# hear we are trying to change the privage variable but it cant change. unless it make new variable with same name but original private variable will not change. it will create new variable with same name but it is not private variable.
print(obj2.__name) 
print(obj2.__dict__)  # hear we can see the private variable in dictionary of object but it is not accessible directly.



obj3 = factory("bike", 500)
# print(obj3.__name)  # hear we try to access the private variable of class but it will not access because it is private variable.
print(obj3.__dict__) 

# encapsulation is only for protecting the variable and method of class from false changes and access
