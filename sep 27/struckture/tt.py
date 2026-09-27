import numpy as np
vector = np.array([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
print(vector[::3])
res=vector[::-1]
print(res)

mas = np.arange(100,116)
print(mas[4::4])
cal=np.arange(105,110)
cal[4::4]=-1
print(cal)