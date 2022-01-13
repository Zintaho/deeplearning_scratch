# 1. Import the numpy package under the name np
import numpy as np

# 2. Print the numpy version and the configuration
print(np.__version__)
np.show_config()

# 3. Create a null vector of size 10
Z = np.zeros(10)
print(Z)

# 4. How to find the memory size of any array
zSize = Z.size * Z.itemsize
print(zSize)

# 5. How to get the documentation of the numpy add function from the command line?
'''python -c "import numpy; numpy.info(numpy.add)'''

# 6. Create a null vector of size 10 but the fifth value which is 1
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 7. Create a vector with values ranging from 10 to 49
Z = np.arange(10, 50)
print(Z)

# 8. Reverse a vector (first element becomes last)
Z = np.arange(50)
Z = Z[::-1]
print(Z)

# 9. Create a 3x3 matrix with values ranging from 0 to 8
Z = np.arange(9).reshape(3,3)
print(Z)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0]
nz = np.nonzero([1,2,0,0,4,0])
print(nz)

# 11. Create a 3x3 identity matrix
Z = np.eye(3)
print(Z)

# 12. Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
print(Z)

# 13. Create a 10x10 array with random values and find the minimum and maximum values
Z = np.random.random((10, 10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

# 14. Create a random vector of size 30 and find the mean value
Z = np.random.random(30)
m = Z.mean()
print(m)

# 15. Create a 2d array with 1 on the border and 0 inside
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
print(Z)

# 16. How to add a border (filled with 0's) an existing array?
Z = np.ones((5, 5))
Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)

# 17. What is the result of the following expression?
0 * np.nan; '''nan'''
np.nan == np.nan; '''False'''
np.inf > np.nan; '''False'''
np.nan - np.nan; '''nan'''
np.nan in set ([np.nan]); '''True'''
0.3 == 3 * 0.1; '''False'''

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+ np.arange(4), k=-1)
print(Z)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern
Z = np.zeros((8,8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
print(np.unravel_index(99, (6,7,8)))

# 21. Create a checkerboard 8x8 matrix using the tile function
Z = np.tile(np.array([[0, 1], [1, 0]]) , (4,4))
print(Z)

# 22. Normalize a 5x5 random matrix
Z = np.random.random((5,5))
Z = (Z - np.mean(Z)) / np.std(Z)
print(Z)

# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA)
color = np.dtype([('r', np.ubyte), ('g', np.ubyte), ('b', np.ubyte), ('a', np.ubyte)])

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
A = np.random.random((5,3))
B = np.random.random((3,2))
Z = np.dot(A, B)
print(Z)

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place.
Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
print(Z)

# 26. What is the output of the following script?
sum(range(5), -1); '''9, numpy not imported'''
sum(range(5), -1); '''10, numpy imported, second argument is axis (negative axis means reverse order)'''

# 27. Consider an integer vector Z, which of these expressions are legal?
Z = np.arange(1, 10)
try:
    Z ** Z; '''legal'''
    2 << Z >> 2; '''legal'''
    Z <- Z; '''legal'''
    1j*Z; '''legal'''
    Z/1/1; '''legal'''
    Z<Z>Z; '''illegal'''
except ValueError:
    pass

# 28. What are the result of the following expressions?
np.array(0) / np.array(0); '''RuntimeWarning: invalid value encountered in true_divide'''
np.array(0) // np.array(0); '''RuntimeWarning: divide by zero encountered in floor_divide'''
np.array([np.nan]).astype(int).astype(float); '''[-2.14748365e+09]'''

# 29. How to round away from zero a float array?
Z = np.random.uniform(-10, +10, 10)
Z = np.copysign(np.ceil(np.abs(Z)), Z)
print(Z)

# 30. How to find common values betwwen two arrays?
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
Z = np.intersect1d(Z1, Z2)
print(Z1, Z2, Z)