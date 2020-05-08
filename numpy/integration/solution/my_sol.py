import numpy as np

def riemann(dx):
    n=np.ceil(np.pi/(2*dx))
    x=np.linspace(0,np.pi/2,num=n)
    s=np.sin((x[1:]+x[:-1])/2)
    print(np.sum(s)*dx)
