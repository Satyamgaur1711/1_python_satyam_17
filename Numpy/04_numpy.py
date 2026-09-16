import numpy as np

x_0 = np.arange(63).reshape((3, 3, 7))
print(f"Data type of x_0 is  {x_0.dtype}")



x_empty = np.empty((1,4), dtype=np.int16)
print(x_empty)
print(f"Deta types of x_empty is {x_empty.dtype}")

# this is how we can make arry and typecast it...
