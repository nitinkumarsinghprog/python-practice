import numpy as np 

# np.arange(1, 11) se array banao.
p1 = np.arange(1, 11)

print(p1)

# Array ko reverse order mein sort karne ka tareeka likho.
a = np.sort(p1)[::-1]
print("revers array : \n", a )

# Array mein har element ko 3 se multiply karo.
c = p1 * 3
print("element multiply : \n", c)

# Array ke even-indexed elements nikaalo.
d = p1[::2]
print("even Indexed : \n", d)

# Do arrays [1, 2, 3] aur [4, 5, 6] ko concatenate karo.
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
e = np.concatenate((a1, a2))
print("Concatenate two array : \n", e)

# Array ko 3 equal parts mein split karo.
arr = np.arange(1,13)
p2 = np.split(arr, 3)
print(p2)

# Array ki copy banao aur copy mein ek value change karo; original check karo.
arr1 = np.array([1,2,3,4,5,6])
# Copy banao
arr2 = arr1.copy()
# Copy mein value change karo
arr2[0] = 99

print("Copy (arr2):", arr2)
print("Original (arr1):", arr1)
