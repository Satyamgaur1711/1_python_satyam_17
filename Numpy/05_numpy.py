import numpy as np

a = np.arange(150).reshape(5,3,10)
# 5 page hai 3 row and 10 column...
print(a)
print(f"dimention of a is {a.ndim}")
b = np.arange(150).reshape(5,3,10)

x = b - a # aishe operation parform karne ke liye dimentin and row column page sabse same hona chahiye.. 
print(x)

w = b**2
print(w)
y = b*2
print(y)

w_y = w/y
print(w_y)

m1 = np.arange(16).reshape(4,4)
print(m1)
m2 = np.array([
    (10,11,12,17),
    (13,14,15,56),
    (16,17,18,10),
    (1,2,3,4)
])
print(m2)
print(m2.ndim)

product = m1.dot(m2)
print(product)
# do arry bana ke matrix manltiplication kar sakty hai.//
