import numpy as np
import matplotlib.pyplot as plt
dx=0.1
x=np.arange(0,np.pi/2,dx)
s=np.sin(x)
ds=(s[2:]-s[:-2])/(2*dx)

c=np.cos(x)
plt.plot(x[1:-1],ds,label='$d/dx(sin)$')
plt.plot(x,c,label='cos')

plt.legend()
plt.show()
