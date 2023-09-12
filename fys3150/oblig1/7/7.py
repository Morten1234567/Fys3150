

import numpy as np
'''

# define matrix A using Numpy arrays
a = np.array([[2, 1, 2],
 [1, 3, 2],
 [1, 0, 0]]) 

#define matrix B
b = np.array([4, 5, 6]) 

x = np.linalg.solve(a, b)
'''




# define matrix A using Numpy arrays
a = np.array([[-2, 1, 0,0],
 [1, -2, 1,0],
 [0, 1, -2,1],[0, 0, 1,-2]]) 

#define matrix B
b = np.array([-0.513, -0.042, -0.0034,-0.0003]) 

x = np.linalg.solve(a, b)

print(x)

# v = [0.43702 0.36104 0.24306 0.12168]

np.savetxt("files2",x)









































