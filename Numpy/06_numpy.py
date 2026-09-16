import numpy as np

a = np.arange(100).reshape(10,10)
b = np.arange(100).reshape(10,10)

x = a.dot(b)
print(x)
y = a@b
print(y)

# koi bhi arry banawo fir matrix multiplication karlo 

c = np.arange(81).reshape(3,3,3,3)
d = np.arange(81).reshape(3,3,3,3)

pro_3D = c@d
print(pro_3D)
