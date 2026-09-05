
def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")    

check(15)

checck = lambda x: print("Even") if x % 2 == 0 else print("Odd")

checck(15)

# Hear both the functions are doing the same thing but the second one is using lambda function which is a way to create anonymous functions in a single line of code.

addition = lambda a, b: a + b
print(addition(10, 15))

# add = lambda *arg: sum = 0 : for i in arg sum+=i 
# iski ganda mara gai. ye itna kaam nahi kar sakta kaam karwane ke liye koi naya rasta dekhna padega

add = lambda *arg: sum(arg) # ye chal jayega
print(add(10, 12, 418, 65,54))
