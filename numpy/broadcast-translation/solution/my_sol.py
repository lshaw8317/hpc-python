import numpy as np
import matplotlib.pyplot as plt
x=np.loadtxt("points_circle.dat")
plt.plot(x[:,0],x[:,1],'o',label='Original')
trans=x+np.array([[2.1,1.1]])
plt.plot(trans[:,0],trans[:,1],'d',label='Translated')
plt.legend()
plt.show()

