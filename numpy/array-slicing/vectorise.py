import numpy
def no_vectorise():
# brute force using a for loop
    arr = numpy.arange(1000)
    dif = numpy.zeros(999, int)
    for i in range(1, len(arr)):
        dif[i-1] = arr[i] - arr[i-1]
def vectorise():
# vectorised operation
    arr = numpy.arange(1000)
    dif = arr[1:] - arr[:-1]

