class dog():
    def speak(self):
        return "bhaanu"

    
class cat():
    def speak(self):
        return "meaaau"

    
class caw():
    def speak(self):
        return "baanaaa"


def voice(animalname):
    print(animalname.speak())

cat = cat()
dog = dog()
caw = caw()


voice(dog)
voice(cat)
voice(caw)




    