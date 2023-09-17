

import numpy as np


#a subdiagonal (under)
# main diagonal (main)
#c superdiagonal (over)


# a b c d
# a b c d
# a b c d
# a b c d


# define matrix A using Numpy arrays

m1=-2
o1=1
c1=0
d1=0
s1=1
m2=-2
o2=1
d2=0
a3=0
s2=1
m3=-2
o3=1
a4=0
b4=0
s3=1
m4=-2

#define diagonal

subd=[s1,s2,s3]
maind=[m1,m2,m3,m4]
overd=[o1,o2,o3]

#define matrix A with the following diagonal

a = np.array([[m1, o1, 0,0],
 [s1, m2, o2,0],
 [0, s2, m3,o3],[0, 0, s3,m4]]) 


#solving the alogithm Av=g

def Axequalsy(a,b):
    return np.linalg.solve(a, b)



b = np.array([-0.513, -0.042, -0.0034,-0.0003]) 


print(Axequalsy(a,b))

#solution

#[0.43702 0.36104 0.24306 0.12168]

#








































































