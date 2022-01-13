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