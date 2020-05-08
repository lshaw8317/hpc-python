cpdef int fibonacci(int n):
    if n==0:
        return 0

    cdef int fnm2=0
    cdef int fnm1=1
    cdef int fn=1
    cdef int i=1
    while i<n:
        fn=fnm1+fnm2
        fnm2=fnm1
        fnm1=fn
        i+=1
    return fn
