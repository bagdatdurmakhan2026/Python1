import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 4], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 12, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
#concatenate обьедение массиво в одного
