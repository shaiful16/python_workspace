import numpy as np


x = np.arange(16).reshape((4,4))

print(x)
print(x.sum(axis=0))  # axis 0 means x axis . that means row
print(x.sum(axis=1))  # axis 1 means y axis . that means column

