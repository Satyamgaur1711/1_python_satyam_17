import numpy as np
import sys

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
