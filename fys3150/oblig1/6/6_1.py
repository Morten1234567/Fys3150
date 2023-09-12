

import numpy as np


#a subdiagonal (under)
# main diagonal (main)
#c superdiagonal (over)


a = np.array([[b1, c1, 0,0],
 [a2, b2, c2,0],
 [0, a3, b3,c3],[0, 0, a4,b4]]) 

def Axequalsy(a,b):
    return np.linalg.solve(a, b)


#define matrix B
b = np.array([-0.513, -0.042, -0.0034,-0.0003]) 

#x = np.linalg.solve(a, b)

print(Axequalsy(a,b))

# v = [0.43702 0.36104 0.24306 0.12168]

#np.savetxt("files2",x)









































