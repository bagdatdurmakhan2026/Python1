import numpy as np

arr = np.array([[1, 2], [3, 4]])

arr = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr, arr), axis=1)

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
# contacatenate also we can use hstack
arr2 = np.array([1, 2, 3])

arr3 = np.array([4, 5, 6])

arr = np.vstack((arr2, arr3))

print(arr)
# vstack also combine array but in colums
arr5 = np.array([1, 2, 3])

arr6 = np.array([4, 5, 6])

arr = np.dstack((arr5, arr6))

print(arr)
# dstack also combine them but in 2 arrayw with respectively positions like 1 to 4 then 2 to 5 so on
arr = np.array([1,2,3,4,5,6,7])
print(arr[2:4])
arr = np.array([1,2,3])
print(np.cumsum(arr))