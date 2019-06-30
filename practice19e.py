import numpy as np

arr = np.loadtxt("data.txt")      # we have to make a file... file is made with the name of data.txt
print(arr)

print("=========================")

# 1-D Array
arr = np.arange(10, 200, 10)
print(arr)
np.savetxt("arraydata.txt", arr)
print("Data Written")

print("==========================")

arr = np.loadtxt("arraydata.txt")
print(arr)