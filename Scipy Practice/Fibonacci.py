from __future__ import division
import numpy
'''
This is a mathematical warm up exercies to calculate
fibonacci sequence
'''

def fib(n=10):
    u_0 = 1
    u_1 = 1
    print u_0
    print u_1
    u_n = [u_0, u_1, 0]
    for i in range (2, n):
        u_n[2] = u_n[1] + u_n[0]
        print u_n[2]
        u_n[0] = u_n[1]
        u_n[1] = u_n[2]

def fib_rec(n=10):
    '''
    Recursive fib implimentation
    '''
    if n<2 :
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

if __name__ == "__main__":
    for i in range(1,10+1):
        val = fib_rec(i)
        print val
