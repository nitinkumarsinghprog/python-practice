#Filtering and calculations

import numpy as np 

p1 = np.array([12, 5, 18, 7, 24, 9, 30])
# [12, 5, 18, 7, 24, 9, 30] se 10 se bade numbers nikaalo.
a = p1[p1 > 10]
print(a)

# Usi array se odd numbers nikaalo.
b = p1[p1 % 2 != 0]
print(b)

# 10 se chhote numbers ko 100 se replace karo.
c = p1.copy()
c[c < 10] = 100
print(c)

# Sum aur mean calculate karo.
d = p1.sum()
print(d)

e = p1.mean()
print(e)

# Maximum aur minimum values ke indexes nikaalo.
f = p1.argmax()
g = p1.argmin()

print(f"Max : {f}, Min : {g}")

# Array mein kitne elements 15 se bade hain, count karo.
ele = (p1 > 15).sum()
print("Count of element greater then 15 : ", ele)

# Array ke unique elements nikaalo.
p2 = np.unique(p1)
print(p2)