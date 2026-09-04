# inharitance mean inhariting property for other class

# code reuseability, more productive 

class animal(): # parant class
    def __init__(self, naam):
        self.name = naam

    def details(self):
        print(f"hallow my name is {self.name}")

class Human(animal): # child class
    print("hallo Human wale animal")


obj1 = Human("aman")
obj2 = Human("gaurang")
obj2.details()
# Human.details() # it dose not work.  isko naam to mila he nahi to kaise print karega









