#1
print("\n1. Import numpy as np and see the version")
import numpy as np
print(np.__version__)

#2
print("\n2. How to create a 1D array?")
arr = np.arange(10)
print(arr)

#3
print("\n3. How to create a boolean array?")
arr2 = np.full((3, 3), True, dtype=bool)
print(arr2)
# Alternate method:
arr3 = np.ones((3,3), dtype=bool)
print(arr3)

#4
print("\n4. How to extract items that satisfy a given condition from 1D array?")
arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arrExtracted = arr4[arr4 % 2 == 1]
print(arrExtracted)
