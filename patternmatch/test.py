import numpy as np

# list = list(zip('abcdefg', range(3), range(4)))
# print(list)

a = np.arange(10)

np.where(a<5, a, 10*a)