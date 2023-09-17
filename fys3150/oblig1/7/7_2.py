
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

a=np.array([s1,s2,s3])
b=np.array([m1,m2,m3])
c=np.array([o1,o2,o3])


d = np.array([-0.513, -0.042, -0.0034]) 
#d = np.array([-0.513, -0.042, -0.0034,-0.0003]) 



import numpy as np

import numpy as np

def TDMA(a,b,c,d):
    n = len(d)
    w= np.zeros(n-1,float)
    g= np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p


print(TDMA(a, b, c, d))

#svar

#[0.4066 0.3002 0.1518]


























