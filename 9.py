#Euler problem 9
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#Algebra: a=a, b=(1000(a-500))/(a-1000), c = 1000-a-b = sqrt(a**2 + b**2)
#Solve for a where all are integers
#Find product abc
import numpy as np

def bFunc(n):
    b = (1000*(n-500))/(n-1000)
    return b

def cFunc1(n):
    c = 1000 - n - bFunc(n)
    return c

def cFunc2(n):
    c = np.sqrt(n**2 + (bFunc(n))**2)
    return c

def pyTrip(n):
    for i in range(1, int(n/3)+1):
        if cFunc1(i) == int(cFunc2(i)):
            return [i, int(bFunc(i)), int(cFunc1(i)), i * bFunc(i) * cFunc1(i)]
