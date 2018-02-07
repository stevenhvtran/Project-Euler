#Euler problem 3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#Returns the smallest divisor of a number that isn't 1
def smallestDiv(lowLim, number):
    for i in range(lowLim,number+1):
        if number%i == 0:
            return i

#Tests whether input is prime
def isPrime(number):
    if smallestDiv(2, number) == number:
        return True
    else:
        return False

#Finds largest prime factor
def largestPF(number):
    
    #Find the smallest divisor of number
    #Check if the quotient is prime
    #If it is then return, if not find the next smallest divisor
    a = 1
    while isPrime(int(number/smallestDiv(a, number))) == False:
        a = smallestDiv(a, number) + 1
    print(number/smallestDiv(a, number))
