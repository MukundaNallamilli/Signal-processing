import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

a=(1+math.sqrt(5))/2
b=(1-math.sqrt(5))/2

def an(n,a,b):
    if n<=0:
        return 0.0
    else:
        return (a**n - b**n )/(a-b)

def bn(n,a,b):
    if n>=1:
        return an(n-1,a,b)+an(n+1,a,b)
    else:
        return 0.0

def f1(n,a,b):
    return an(n+2,a,b)-1


n=np.arange(1,12)
vec_an=scipy.vectorize(an)

# summation of ak 
def f2(n,a,b):
    return np.sum(vec_an(np.arange(1,n+1),a,b))


vec_f1=scipy.vectorize(f1)
vec_f2=scipy.vectorize(f2)
l1=vec_f1(n,a,b)
l2=vec_f2(n,a,b)

markerline1,streamline1, _ = plt.stem(n,l1,label=r'$a_{n+2}-1$')
markerline2,steamline2,_ = plt.stem(n,l2,label=r'$\sum_{k=1}^{n}a_{k}$')
plt.setp(markerline1, 'markerfacecolor', 'b')
plt.setp(markerline2, 'markerfacecolor', 'r')
plt.grid()
plt.legend()
plt.savefig('../figs/1_1.png')
plt.show()


