import numpy as np

a=np.random.randn(8,8)
a1,a2=np.split(a,2,axis=0)
print('Ex. 1')
print(a1.shape,a2.shape)
a_new=np.concatenate((a1,a2),axis=0)
print(a_new.shape)

print('Ex. 2')
a1=np.zeros((8,4))
a2=np.zeros((8,4))
a_new=np.concatenate((a1,a2),axis=1)
print(a_new.shape)


