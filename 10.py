#Euler problem 10
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

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

'''
FAILED ATTEMPT AT OPTIMISATION OF NPRIME(N)

listPrimes=[2,3]
#Can't even use this, its depended on nprime2()
def isPrime2(n):
    #Checks for primality by determining if there is a prime composition
    for i in listPrimes:
        if i > int(np.sqrt(n))+1:
            return True
        if n%i == 0:
            return False
    return True

#Slower than nPrime()
def nPrime2(n):
    global listPrimes
    listPrimes = [2,3]
    #Starts primes at 2 to account for exceptions to 6n+-1 rule
    p = 2
    #Starts number to be subbed into plusPrime and minusPrime to 0
    pmPrime = 0
    #Holds the state of last used generator of possible primes
    pmState = 0

    #Checks for primes in generated numbers, stops when n'th prime is found
    while p < n:
        pmPrime += 1
        if isPrime2(minusPrime(pmPrime)) == True:
            listPrimes.append(minusPrime(pmPrime))
            pmState = -1
            p += 1
        if isPrime2(plusPrime(pmPrime)) == True and p<n:
            listPrimes.append(plusPrime(pmPrime))
            pmState = +1
            p += 1            
    #Returns n'th prime using generator number and states
    return (6*pmPrime + pmState)
'''

#Finds the sum of all the primes up to and including n
def sumPrime(n):
    currentPrime = 0
    total = 5
    pmPrime = 0
    while n > currentPrime:
        pmPrime += 1
        if isPrime(minusPrime(pmPrime)) == True:
            currentPrime = minusPrime(pmPrime)
            if currentPrime>n:
                break
            total += currentPrime
        if isPrime(plusPrime(pmPrime)) == True and currentPrime < n:
            currentPrime = plusPrime(pmPrime)
            if plusPrime(pmPrime)>n:
                break
            total += currentPrime
    return(total)

