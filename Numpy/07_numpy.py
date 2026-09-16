import numpy as np

rg = np.random.default_rng(100)  # create instance of default random number generator sayad isse random number generate hoty hai...
a = np.ones((2, 3,2), dtype=np.int_)
b = rg.random((2, 3))
print(a)
print(b)
print(rg)
