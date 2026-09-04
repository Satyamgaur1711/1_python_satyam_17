# constructor in inharitance

class bag():
    def __init__(self, material, zip, volume):
        self.material = material
        self.zip = zip
        self.volume = volume

    def detailes(self):
        print(f"you bag are made of of {self.material}, and your bag hai {self.zip} zips, {self.volume} leter is the size of the bag \n")

# first of all define funtion and define class:
# rebock class sare function ko inharit kar sakti hai. or usme add bhi kar sakti hai
class rebock(bag):
    def __init__(self, material, zip, volume, color):
        super().__init__(material, zip, volume)
        self.color = color
# yaha super() funtion ke wajah se material zip and volume apne aap parnat se mil gaye for color hame add kar diya to def init to bana padega sare paramiter likhne padengye. par paramiter ke value ko firse self.paramiter nahi kana padega. ha jo new paramiter add kiye and usko firse self.newparamiter karna padega.

    def detailes(self):
        print(f"the color of my bag rebok bag  is {self.color}")
        return super().detailes()
# same hear, details ka method parant me hone ke wajah se direct use kar sakty hai. baki ke print statments nahi likhni padegi.


# pahle objet banawo fir usi objcect ke thruough method ko call kardo.
normalbag = bag("lether", 4, 55)
# hear how call a method.
normalbag.detailes()

rebobag = rebock("polister", 7, 80, "pink")
rebobag.detailes()


       