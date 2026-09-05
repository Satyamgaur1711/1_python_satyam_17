# abstraction mean hiding the implementation details and showing only functionality to the user. jaishe bike ke andar engin karishe kam kar raha hai ye pata user ko batane ke jaruat nahi hai wo sirf functionality ke bare me janna chahata hai ki bike chal rahi hai ya nahi. yehi abstraction ka main concept hai.

from abc import ABC, abstractmethod


class functionality(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# abstractmethod decorator ke hone se child class ko strictly ye method ko banana he padega. agar child class aishe na kare to object create he nahi ho payega.

class bike(functionality):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        pass
    def stop(self):
        pass


obj1 = bike("pulsar", "black") 

print(obj1.name, obj1.color)  