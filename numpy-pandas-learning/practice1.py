import numpy as np

# Q1. 1 se 50 tak ke numbers ka array banao (arange se).

print("Q1:", np.arange(1, 51))

# Q2. 0 aur 1 ke beech 20 equally spaced numbers banao (linspace se).
print("Q2:", np.linspace(0, 1, 20))

# Q3. 4x4 matrix banao jisme sab values 5 hon (full se).
print("Q3:\n", np.full((4, 4), 5))

# Q4. 3x3 identity matrix banao (eye se).
print("Q4:\n", np.eye(3))

# Q5. 1 se 100 ke beech 10 random integers generate karo, seed=42 set karke (random se).
np.random.seed(42)
print("Q5:", np.random.randint(1, 101, 10))

# Q6. Ek existing array a = np.array([10, 20, 30]) banao, phir uske shape ka zeros_like banao.
a = np.array([10, 20, 30])
print("Q6:", np.zeros_like(a))

# Q7. 0 se 5 tak 0.5 ke step se array banao (arange se).
print("Q7:", np.arange(0, 5.5, 0.5))

# Q8. 6x6 matrix banao jisme diagonal pe 1 ho aur baaki sab 9 ho.
arr = np.full((6, 6), 9)
np.fill_diagonal(arr, 1)
print("Q8:\n", arr)

# Q9. 2x3 ka array banao jisme sab True ho (boolean dtype).
print("Q9:\n", np.full((2, 3), True))

# Q10. np.linspace(0, 10, 5, retstep=True) ka output kya aayega? Pehle guess karo, phir chalao.
print("Q10:", np.linspace(0, 10, 5, retstep=True))
