# polymorphisam

def hallow():
    print("hallow bor")

def hallow():
    print("hallow bro how are you.")


hallow()

# hear are 2 function but we cannot call both at once. dushar function overright kar dega first wale funcion.


class animal():
    def fly(self):
        print("No we are animal we cannot fly.")

class bird():
    def fly(self):
        print("Yes we are bird we can fly")

obj = animal()
obj1 = bird()

obj.fly()
obj1.fly()

# this is polymorphisium. fly function se do output le sakty hai. 


# Method overwring (we need inharitance)

class school():
    def __init__(self, name):
        self.name = name

    def detail(self):
        print(f"my name is {self.name}")

class classs(school):
    def __init__(self, name):
        super().__init__(name)

    def detail(self):
        print(f"my name is {self.name}, theis only detail i have")

# Yaha ek method dushre method ko over right kar deta hai. jo last me likha jata hai kyuke python is a interpreter language.

obj4 = classs("Btech")
obj4.detail()



# Method overloading 

class roommate():
    def __init__(self, name):
        self.name = name
        print("hallow how are you")

    def __init__(self, name, a, b):
        print("my name is rangdaar.")


obj5 = roommate("aman", "good", "ladki ke tarah")

# saidly method overloading dose not exit in python because python is interpriter language
