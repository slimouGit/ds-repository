#1
print("\n1. Import numpy as np and see the version")
import numpy as np
print(np.__version__)

#2
print("\n2. How to create a 1D array?")
arr = np.arange(10)
print(arr)

#3
print("\n3. How to create a boolean array?")
arr = np.full((3, 3), True, dtype=bool)
print(arr)
# Alternate method:
arr = np.ones((3,3), dtype=bool)
print(arr)

#4
print("\n4. How to extract items that satisfy a given condition from 1D array?")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
arrExtracted = arr[arr % 2 == 1]
print(arrExtracted)

#5
print("\n5. How to replace items that satisfy a condition with another value in numpy array?")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
arr[arr % 2 == 1] = -1
print(arr)

#6
print("\n6. How to replace items that satisfy a condition without affecting the original array?")
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

#7
print("\n7. How to reshape an array?")
arr = np.arange(10)
print(arr)
arrReshaped = arr.reshape(5, -1)
print(arrReshaped)

#8
print("\n8. How to stack two arrays vertically?")
a = np.arange(10).reshape(2,-1)
print(a)
b = np.repeat(1, 10).reshape(2,-1)
print(b)
print(np.concatenate([a, b], axis=0))
print(np.vstack([a, b]))

#9
print("\n9. How to stack two arrays horizontally?")
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print("a ",a)
print("b ",b)
print("1. ", np.concatenate([a, b], axis=1))
print("2. ", np.concatenate(np.hstack([a, b])))
print("3. ", np.concatenate(np.c_[a, b]))

#10
print("\n10. How to generate custom sequences in numpy without hardcoding?")
a = np.array([1,2,3])
print("a ",a)
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])
print(np.r_[np.repeat(a, 4), np.tile(a, 4)])

#11
print("\n11. How to get the common items between two python numpy arrays?")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#Desired Output: array([2, 4])
print(np.intersect1d(a,b))

#12
print("\n12. How to remove from one array those items that exist in another?")
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
#Desired Output: array([1,2,3,4])
print(np.setdiff1d(a,b))

a = np.array(["milk","coffee","water"])
b = np.array(["cola","water"])
#Desired Output: array([milk,coffee])
print(np.setdiff1d(a,b))

#13
print("\n13. How to get the positions where elements of two arrays match?")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#Desired Output: (array([1, 3, 5, 7]),)
print(np.where(a == b))

#14
print("\n14. How to extract all numbers between a given range from a numpy array?")
a = np.array([2, 6, 1, 9, 10, 3, 27])
#Get all items between 5 and 10 from a
index = np.where((a >= 5) & (a <= 10))
print("1. ", a[index])

index = np.where(np.logical_and(a>=5, a<=10))
print("2. ", a[index])

print("3. ", a[(a >= 5) & (a <= 10)])

#15
print("\n15. How to make a python function that handles scalars to work on numpy arrays?")
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

print(maxx(1, 5))

pair_max = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))

#16
print("\n16. How to swap two columns in a 2d numpy array?")
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:, [1,0,2]])

#17
print("\n17. How to swap two rows in a 2d numpy array?")
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[[1,0,2], :])
print(arr[[2,1,2], :])

#18
print("\n18. How to reverse the rows of a 2D array?")
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[::-1])

#19
print("\n19. How to reverse the columns of a 2D array?")
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:, ::-1])

#20
print("\n20. How to create a 2D array containing random floats between 5 and 10?")
arr = np.arange(9).reshape(3,3)
print("1. ", np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3)))
print("2. ", np.random.uniform(5,10, size=(10,2)))

#21
print("\n21. How to print only 3 decimal places in python numpy array?")
rand_arr = np.random.random((5,3))
print(rand_arr)
rand_arr = np.random.random([5,3])
print(rand_arr)
print(np.set_printoptions(precision=3))
print(rand_arr[:4])

#22
print("\n22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?")
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
print(np.set_printoptions(suppress=False))
print(np.random.seed(100))
print(np.random.random([3,3])/1e3)

#23
print("\n23. How to limit the number of items printed in output of numpy array?")
a = np.arange(15)
print(a)

np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)

#24
print("\n24. How to print the full numpy array without truncating")
np.set_printoptions(threshold=10)
b = np.arange(15)
print(b)

np.set_printoptions(threshold=np.nan)
print(b)

#25
print("\n25. How to import a dataset with numbers and texts keeping the text intact in python numpy?")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

print(iris[:3])






