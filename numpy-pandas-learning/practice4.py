import numpy as np

# Indexing + Slicing
print("\n" + "=" * 40)
print("SECTION 2: INDEXING + SLICING")
print("=" * 40)

a = np.arange(1, 25).reshape(4, 6)  
print("Base array:\n", a)

# P1: Pehla element (row 0, col 0) nikaalo
print()
print("Element (row 0, col 0) :", a[0,0])

# P2: Poori row 2 nikaalo
print()
print("Poori row 2 : \n", a[2])

# P3: Poora column 3 nikaalo
print()
print("Poora column 3 : \n", a[:,3])

# P4: Top-left 2x3 block nikaalo
print()
print("Top_left 2X3 block : \n", a[:2,:3])

# P5: Bottom-right 2x2 block nikaalo
print()
print("Bottom-right 2X2 : \n", a[2:, 4:])

# P6: Last row nikaalo
print()
print("last row : \n", a[-1])

# P7: Har row ka pehla element nikaalo
print()
print("Har row ka pehla element : \n", a[:, 0])

# P8: Har doosra row nikaalo (step use karo)
print()
print("Har doosra row : \n", a[::2, :])

# P9: Har row ke first 3 columns
print()
print("Har row ke first 3 columns : \n", a[:, :3])

# P10: Ek 1D array banao [10,20,30,40,50,60] aur usme se [20,40,60] nikaalo
p1 = np.array([10,20,30,40,50,60])
print()
print("matrix \n", p1[1::2])
