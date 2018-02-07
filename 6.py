#Euler problem 6
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

#Finds the sum of squares from a range
def sumSquares(low, high):
    number = 0
    for i in range(low, high+1):
        number += (i**2)
    return(number)

def squareSum(low, high):
    number = 0
    for i in range(low, high+1):
        number += i
    return number**2
