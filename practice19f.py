import numpy as np

arr1 = np.arange(10, 21)
print(arr1)

print()

arr2 = np.arange(10, 31, 22)
print(arr2)

print()

arr3 = np.ones((3,3), dtype=int)
arr3[0][2] = 4
print(arr3)

print()

arr4 = np.linspace(0, 21, 4)
print(arr4)