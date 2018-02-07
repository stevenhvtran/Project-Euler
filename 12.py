#Euler problem 12
'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import numpy as np 

#Finds divisors of numbers
def divisors(n):
    div = 0
    for i in range(1, n+1):
        if n%i == 0:
            div += 1
    return div

#Finds n'th triangle number
def triangle(n):
    total = 0
    for j in range(0, n+1):
        total += j
    return total

#Finds first triangle number with over n divisors
def divTri(n):
    m=1
    while divisors(triangle(m)) <= n:
        m+=1
    return triangle(n)
