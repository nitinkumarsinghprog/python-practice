import numpy as np

print("=" * 40)
print("SECTION 1: SHAPE + RESHAPE")
print("=" * 40)

#P1: 1 se 24 tak array banao, phir 4x6 mein reshape karo
p1 = np.arange(1, 25)
print(p1)
print()
print("Reshape to 4X6")
print(p1.reshape(4,6))

# P2: Us 4x6 array ko 6x4 mein reshape karo
print()
print("Reshape to 6X4")
print(p1.reshape(6,4))

# P3: Us array ko 2x12 mein reshape karo
print()
print("Reshape to 2X12")
print(p1.reshape(2,12))

# P4: Us array ko 2x3x4 (3D) mein reshape karo — shape check karo
print()
print("Reshape to 2X3X4")
print(p1.reshape(2,3,4))

# P5: 3x3 identity matrix banao, usko flatten karo
print()
print("3X3 identity matrix")
p2 = np.eye(3)
print(p2)
print(p2.flatten())

# P6: 1D array [1,2,3,4,5,6] se 2x3 banao, phir transpose karo
print()
print("2X3 matrix")
p3 = np.array([1,2,3,4,5,6])
print(p3.reshape(2,3))
print()
print("Transpose")
print(p3.reshape(2,3).T)


# P7: reshape(-1, 4) ka use karke 2x4 array banao 8 elements se
print()
print("2X4 reshape matrix")
p4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(p4.reshape(-1, 4))

# P8: Ek 2D array banao, uski shape, ndim, size print karo
print()
p5 = np.array([[1,2,3,4],[5,6,7,8]])
print(p5.shape)
print(p5.ndim)
print(p5.size)

