import numpy as np

arr = np.arange(10, 51, 3)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

# Acess Array Elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[:3])
print(arr[:5])
print(arr[3:5])

slices = slice(1, 20, 2)
print(slices)
print(arr[slices])

arr2D = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])
print(arr2D)
print(arr2D.shape)
print(arr2D.ndim)


print()
print(arr2D[0][1])
print()
print(arr2D[0:2])
print()
print(arr2D[0:2, 0:2])
print()
print(arr2D[0, 1])   # equal to print(arr2D[0][1])
