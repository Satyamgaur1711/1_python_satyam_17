import numpy as np
print(np.__version__)

a = np.arange(20).reshape(5,4)



# print(a)
print(a.ndim) # use to find dimention of arry 
print(a.dtype.name) 
print(a.dtype)

print(a.dtype.alignment)
print(a.shape) # use to find the shape (ketne cross kiene ka hai) of arry
print(a.size) # use to find the size of arry
print(f"the size of bytes fo each element is {a.itemsize}") 
print(f"Pata nahi kaha ke location de raha hai ye  {a.data}")

print(f"ye python ka buildit funtion se a ka type print kiya hai {type(a)}") 

new_arry = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"This is the new arry creted by np {new_arry}")

# array creation...
float_wali_arry = np.array([1.0, 2,3,4,5,6,7,8.9,10])
print(f"agar arry me koi bhi element float hu to float detatype he ayega {float_wali_arry.dtype}")

# array() take form 1 to 2 positional arguments..

# x = np.array(1, 2, 3, 4, 12)
# Hear 5 argument are given to the arry that's error

x = np.array([(1,2,3,4,5,6), (8,9,10,11,12,13)])
print(x)

# aishe use karengy be awere number of number shoulb be same...
