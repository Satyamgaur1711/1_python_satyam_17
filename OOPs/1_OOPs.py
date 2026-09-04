class student:
    name = "satyam gaur"
    age = 34
    college = "BIET jhansi"
# hear all this attribute are class attribute.
# a attribute belong to tha class not for object called class attribute.
    def sum(x, y): # this are method
        print("this is a part of method in class")
        return x +y
    def collagedetail():
        print("bahot bada chutiya college hai.")
    


satyam = student()
satyam.village = "sikandarpur"
# hear satyam.village is a object attribute/ instance attribute.
satyam.name = "Er. Satyam gaur"
# ye ek instance attribute iski prefirance jyda hai class attribute
print(satyam.name, satyam.age , satyam.college, satyam.village)

number = student.sum(15, 15) # yaha deko function ko direct class ke through call kiya gaya hai isliy sefl ke koi jarurat nahi padi


print(number)

detail = student.collagedetail()# yaha deko function ko direct class ke through call kiya gaya hai isliy sefl ke koi jarurat nahi padi
print(detail)
student.collagedetail()

# agar funcion ko object ke through call karu to.
# satyam.collagedetail()
# yaha py self dena padega.

