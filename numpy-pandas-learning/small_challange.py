
import numpy as np

# Challenge: np.arange se 1..12 banao
a = np.arange(1,13)
print(a)

# 1. 3x4 mein reshape karo
b = a.reshape(3,4)
print("Reshape")
print(b)

# 2. Uska transpose karo (4x3)
c = b.T
print("Transpose")
print(c)

# 3. Transpose ko wapas flatten karo
d = c.flatten()
print("flatten")
print(d)

# 4. Flatten ka shape kya hai?
e = d.shape

print(e)

# 5. Original 3x4 aur transpose 4x3 ka .shape compare karo
print("Original b shape (3x4):", b.shape)   # (3, 4)
print("Transpose c shape (4x3):", c.shape)  # (4, 3)
print("Flatten d shape:", d.shape)          # (12,)

