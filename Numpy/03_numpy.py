import numpy as st

x = st.array([[1,2,3,4,5,6], [7,8,9,10,11,12] ], dtype=st.complex128)
# ye 2d hai ek page hai ye agar bracket lagake ek page or add kardu to 3d ho jayegi

print(f"The detatype if {x.dtype}")
print(f"The dimentin is {x.ndim}")
print(f"The size and shape is {x.size}, {x.shape}")
print(x)
# dtype=st.complex128  ye batata hai arry me complex number hai 128 batata hai ke system me unko kitna space dena hai.. int me 64 aata tha and isme 128 aayega.. or float me bi 64 aata tha..
# or ha yaha number ke jagah charector add kane ke koshish mat karna.. 

