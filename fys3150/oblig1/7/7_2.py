
import numpy as np



def thomas(a,b,c,d):
    n = len(b)
    if len(a) != n-1:
        print ('Wrong index size for a.\n A should have an index of', n-1, '\n Your a has ', len(a))
          

    if len(c) != n-1:
        print ('Wrong index size for c.\n C should have an index of', n-1, '\n Your c has', len(c))



    for i in range(0,len(a)):
        a[i] = float(a[i])
    for i in range(0,len(b)):
        b[i] = float(b[i])
    for i in range(0,len(c)):
        c[i] = float(c[i])
    for i in range(0,len(d)):
        d[i] = float(d[i])
    c.append(0.0) # Hack to make the function to work


    p = []; q= [] 
    p.append(c[0]/b[0]); q.append(d[0]/b[0])
    for j in range(1,n):
        pj = c[j]/(b[j] - a[j-1]* p[j-1])
        qj = (d[j] - a[j-1]*q[j-1])/(b[j] - a[j-1]* p[j-1])
        p.append(pj); q.append(qj)

    x = []; x.append(q[n-1])
    for j in range(n-2,-1,-1):

        xj = q[j] - p[j]*x[0]  # Value holder
        x.insert(0,xj)   # Building the list backwards
    return x


#!/usr/bin/python

# Import the function:
# Matrix
a= [1,1,1]

b= [-2,-2,-2,-2] 
c= [1,1,1]
d= [-0.513, -0.042, -0.0034,-0.0003]
# Execute the function
x = thomas(a,b,c,d)
# Print the result
print (x)



#[-2, 1, 0,0],
#[1, -2, 1,0],
#[0, 1, -2,1],
#[0, 0, 1,-2]]) 


#b = np.array([-0.513, -0.042, -0.0034,-0.0003]) 



#[0.43701999999999996, 0.3610399999999999, 0.24305999999999994, 0.12167999999999997]
















