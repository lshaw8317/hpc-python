import numpy

x=numpy.loadtxt("xy-coordinates.dat")
x[:,1]+=2.5
numpy.savetxt("new_xy-coordinates.dat",x,fmt='%7.3f')
