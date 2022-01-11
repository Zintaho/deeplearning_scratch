# 1. Import the numpy package under the name np
import numpy as np

# 2. Print the numpy version and the configuration
print(np.__version__)
np.show_config()

# 3. Create a null vector of size 10
a = np.zeros(10)
print(a)

# 4. How to find the memory size of any array
aSize = a.size * a.itemsize
print(aSize)

# 5. How to get the documentation of the numpy add function from the command line?
np.info(np.add)

# 6. Create a null vector of size 10 but the fifth value which is 1
b = np.zeros(10)
b[4] = 1
print(b)

# 7. Create a vector with values ranging from 10 to 49
c = np.arange(10, 50)
print(c)

# 8. Reverse a vector (first element becomes last)
d = np.flip(c)
print(d)

# 9. Create a 3x3 matrix with values ranging from 0 to 8
e = np.arange(0,9).reshape(3,3)
print(e)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0]
f = np.array([1,2,0,0,4,0])
print(np.where(f != 0))
