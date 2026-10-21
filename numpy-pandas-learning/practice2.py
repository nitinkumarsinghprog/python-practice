import numpy as np


#Q1 10 se 50 tak even number generate karo 
num = np.arange(10, 50, 2)
print(num)

#Q2 array diya hain max, min and avrage nikalna hain 
marks = np.array([45, 80, 65, 90, 35])
print(f"Min number : {marks.min()}")
print(f"Max number : {marks.max()}")
print(f"Avarage : {marks.mean()}")

#Q3 Indexing aur Slicing
num1 = np.array([10, 20, 30, 40, 50, 60])
print(num1[1:4])
print(num1[4:])

#Q4 Boolean Indexing
marks1 = np.array([25, 60, 85, 40, 95, 30])
print(marks1[marks1 > 50])

#Q5 Reshape
n = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(n.reshape(3,4))