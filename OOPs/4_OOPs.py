class animal():

    kingdome = "earth_py_rahne_wale"


    def __init__(self, A_name, A_legs, A_tell):
        self.color = "hariyar" # this is a class attribute.
        self.name = A_name # these are the object/instance attributes
        self.legs = A_legs # these are the object/instance attributes
        self.tall = A_tell # these are the object/instance attributes

    def abt(self): # instance/object method & capture the location of object:
        print(f"this is a good animal and have a cute smile name {self.name}")

    @classmethod 
    def details(cls):# capute the location of class
        print(f"how are you, i kingdome is {cls.kingdome}")
    @staticmethod
    def static():
        print("I am a static method. you can call me form class and object")



        
anamRaja = animal("aman", 4, True)

print(anamRaja.name, anamRaja.tall, anamRaja.legs, anamRaja.abt)
anamRaja.details()

animal.static()
anamRaja.static()

# anamRaja.kingdome() ye dono nahi chal rahe.
# animal.kingdome() ye bhi nahi.

# str = animal.kingdome()
# print(str)                 not working 

# str = anamRaja.kingdome()
# print(str)                not working 
