import numpy as np

arr = np.array([10, 20, 30, 40, 45, 66, 77])
print(arr)
arr2 = np.array([[10, 20, 30], [20, 30, 40]])
print(arr2)

print(arr2[0, 1])
print(arr[1])

print(arr.ndim)
print(arr2.ndim)

print(arr[0:3])
print(arr[:5])

newarr = arr.copy()
print(newarr)
