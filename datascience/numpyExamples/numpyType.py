
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"


b = np.array([[1,2,3],[4,5,6]])    # [[row0][row1]]
print(b.shape)                     # Prints "(2, 3)"
