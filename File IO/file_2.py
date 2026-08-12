f = open("file_lines.txt")
liness = f.readlines()
print(liness)
print(type(liness))


# if read line ka use kar to ek line milegi or agar lines ka use kro sari milegiz

line1 = f.readline()
print(line1 , type(line1)) 

line2 = f.readline()
print(line2, type(line1))

line3 = f.readline()
print(line3, type(line1))

line4 = f.readline()
print(line4, type(line1))
f.close()
# yaha py ek baar sare line ko read kar lene ke baad koi line bahchi he nahi to line1234 me sirf empty string aa raha hai.


# wapa se use karne ke liye file ko close karke firse open karna padega

g = open("file_lines.txt")

line1 = g.readline()
print(line1 , type(line1)) 

line2 = g.readline()
print(line2, type(line1))

line3 = g.readline()
print(line3, type(line1))

line4 = g.readline()
print(line4, type(line1))

g.close()




k = open("file_lines.txt")
line = k.readline()

while line != "":
    print(line)
    line = k.readline()