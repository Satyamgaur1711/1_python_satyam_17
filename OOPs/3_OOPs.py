class car():
    def __init__(self, body, color, engin):
        self.body = body
        self.color = color
        self.engin = engin


toyota = car("suv", "Red", "V16")
tata = car("Tank", "Black", "V24")
print(toyota.color)
print(tata.color)

# Hear funtion ka jo self paramiter hai wo toyota variable ke position leta hai
# position lene ke bad wo waha py body color engin assign karta hai.
# let suppose totyota ke postion 101010 hai.
# 101010.color = Red
# 101010.engin = V16
# 101010.body = "suv"
# aishe karke asign karta hai,

