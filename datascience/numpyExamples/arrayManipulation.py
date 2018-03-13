
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array

print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"


b = np.array([[1,2,3],[4,5,6]])    # [[row0][row1]]
print(b[0, 0], b[0, 1], b[0, 2])
print(b[1, 0], b[1, 1], b[1, 2])