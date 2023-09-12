
from matplotlib.pyplot import *
import numpy as np





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

subd=[s1,s2,s3]
maind=[m1,m2,m3,m4]
overd=[o1,o2,o3]



a = np.array([[m1, o1, 0,0],
 [s1, m2, o2,0],
 [0, s2, m3,o3],[0, 0, s3,m4]]) 




def Axequalsy(a,b):
    return np.linalg.solve(a, b)



b = np.array([-0.513, -0.042, -0.0034,-0.0003]) 


g =1
d =1
XX =1
YY =1


T = 10
N = 10


z0=np.zeros(2)
z0[0] = 2.0

kol1=np.sqrt(1)
kol2=np.sqrt(1)

Ndts=4 
legends=[]
error_diff=[]

def f(z, t):

    x = np.zeros_like(z)
    α=XX/(YY*d)
    x[:]=[z[1],g-α*z[1]]
    return x 

def matrix(func,z0, TIME):

    z=np.zeros((np.size(TIME),np.size(z0)))
    z[0,:]=z0  

    for i in range(len(TIME)-1):
        dt=TIME[i+1]-TIME[i]
        z[i+1,:]=z[i,:]+np.asarray(func(z[i,:],TIME[i]))*dt
    return z


for i in range(Ndts+1):

    TIME=np.linspace(0,T,N+1)
    sm=matrix(f,z0,TIME)
    v_a=kol1*np.tanh(kol2*TIME)

    absolute_error=np.abs(sm[:,1]-v_a)
    log_error=np.log2(absolute_error[1:])
    max_log_error=np.max(log_error)
    
    plot(TIME[1:],log_error)
    legends.append('N '+str(N)+'t/s')
    N*=2
    if i>0:
        error_diff.append(previous_max_log_err-max_log_error)

    previous_max_log_err=max_log_error
    
print('Approximate=',np.mean(error_diff))
print('Approximateerror',1/2**(np.mean(error_diff)))


legend(legends,loc='best',frameon=False)
xlabel('s')
ylabel('logtwo-error')
show()
