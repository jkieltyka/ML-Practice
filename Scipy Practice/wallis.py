from __future__ import division
import numpy
'''
This is a mathematical warm up exercies to calculate
PI using the Wallis formula
'''
def wallis(n):
    pi = 1.0
    for i in range(1, n+1):
        top = 4 * i**2
        bottom = (4 * i**2) - 1
        pi = pi * (top / bottom)
    pi = 2 * pi
    return pi

if __name__ == "__main__":
    val = wallis(1000000)
    print val
