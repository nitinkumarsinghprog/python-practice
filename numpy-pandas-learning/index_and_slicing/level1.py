import numpy as np

# [5, 10, 15, 20, 25] array banao.
p1 = np.arange(5,30,5)

print(p1)

# Iska third element nikaalo.
a = p1[2]
print("Third Element : ", a)

# Last element negative indexing se nikaalo.
b = p1[-1]
print("last element : ", b)

# [10, 15, 20] slicing se nikaalo.
c = p1[1:4]
print(c)

# First 3 elements nikaalo.
d = p1[:3]
print("First 3 element",d)

# Last 2 elements nikaalo.
e = p1[-2:]
print("last 2 element : ", e)

# Har doosra element nikaalo.
f = p1[0::2]
print("Har doosra element : ", f)

# Array ko reverse karo.
g = p1[::-1]
print("Reverse : ", g)