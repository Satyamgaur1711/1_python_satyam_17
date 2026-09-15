import numpy as np

a = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(a)
print(f"Size of a is {a.size}")
print(f"Shape of a is {a.shape}")
print(f"Dimention of a is {a.ndim}")
# a is not 3 D arry it is 2 dimentin arry with 3 row and 3 column

# let's create 3 dimentin arry..



b = np.array([1,2,3])
print(f"Dimention of b is {b.ndim}")
print(b)

c = np.array([
    (1,2,3), (4,5,6)
    ])
print(f"Dimention of c is {c.ndim}")
print(c)



x = np.array([
     [
        (1,2,3,10),   # ye first page hai jaha py 3 row and 4 column hai...
        (4,5,6,11),   # ye first page hai jaha py 3 row and 4 column hai...
        (7,8,9,12)    # ye first page hai jaha py 3 row and 4 column hai...
     ],
     [
        (15,25,35,150),  # ye second page hai page hai jaha py 3 row and 4 column hai...
        (45,55,65,151),  # ye second page hai page hai jaha py 3 row and 4 column hai...
        (75,85,95,152)   # ye second page hai page hai jaha py 3 row and 4 column hai...
     ]
    ])
print(f"Dimention of x is {x.ndim}")
print(x.size)
print(x.shape)
print(x)
print(f"The deta type 3D x array is {x.dtype}")

