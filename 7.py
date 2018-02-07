#Euler problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

'''
THIS CODE IS VERY CRAP. DONT USE IT FOR GENERAL PURPOSES, ISPRIME DOESNT EVEN WORK PROPERLY FOR 2,
CODE WAS WRITTEN FOR SPEED OF FINDING NPRIME(N)
'''

#Produce numbers that can be prime i.e. 6n +- 1
#Check if they are prime
#Increment counter if they are
#When the 10001st one is reached return it

import numpy as np

#Generate numbers that can actually be prime (exclude 2,3)
def plusPrime(n):
    return 6*n + 1
def minusPrime(n):
    return 6*n - 1

#Checks for primality, doesn't work for numbers < 3
def isPrime(n):
    #Discards even numbers
    if n%2 == 0:
        return False
    #Checks for primality by determining if there is a divisor up to sqrt(n)+1
    for i in range(3,int(np.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

#Finds the n'th prime, doesnt work for n < 3
def nPrime(n):
    #Starts primes at 2 to account for exceptions to 6n+-1 rule
    p = 2
    #Starts number to be subbed into plusPrime and minusPrime to 0
    pmPrime = 0
    #Holds the state of last used generator of possible primes
    pmState = 0

    #Checks for primes in generated numbers, stops when n'th prime is found
    while p < n:
        pmPrime += 1
        if isPrime(minusPrime(pmPrime)) == True:
            pmState = -1
            p += 1
        if isPrime(plusPrime(pmPrime)) == True and p<n:
            pmState = +1
            p += 1

    #Returns n'th prime using generator number and states
    return (6*pmPrime + pmState)

