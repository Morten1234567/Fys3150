

import numpy as np



import matplotlib.pyplot as plt


z=int(1E2)
x=np.linspace(0,1,z)


def f(x):
    return (x)/(np.exp(10)) - x - np.exp(-10*x) + 1

y=f(x)
plt.plot(x,f(x))
#plt.show()


xx=[]
yy=[]
#q=("%.3f" % x[0])


for i in range(len(x)):
    xx.append(np.format_float_scientific(x[i]))
    yy.append(np.format_float_scientific(y[i]))



#yy=np.format_float_scientific(f(x))



#print(int(xx[-2]))

#xxx=np.array((yy))
#yyy=np.array((xx))

#print(xxx)

#print(xxx)
#print(xxx[-2])
#print(f'{x:.3f}')
#print(q)


#xxxx=("%.1f" % xxx[0])
#print(xxxx)


data = np.column_stack((xx,yy))

#print(type(data))
#qq=((data[-2][0]))

#print(qq)

#print(type(data[-2][0]))

#print(type(data[-2][0]))

np.savetxt("files.txt",data, delimiter=" ", fmt="%s")


'''
qq=[]

#print(data[:,0])

#print(data[0])
for i in range(len(data[:,0])):
    qq.append(data[i])


a = open("files.txt","w")
a.write(str(qq))

print(data[-2])

'''























