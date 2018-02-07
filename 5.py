#Euler problem 5
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#Tests if a number is evenly divisible by all the numbers in a range
def divRan(num, low, high):
    #Returns a list with pos 0 either true or false and pos 1 the smallest divisor
    for i in range(low, high):
        if num%i != 0:
            return [False, i]
    return [True, num]

#Selects a number that IS evenly divisible by a range from a seed number (should be composite)
def overestimate(num, low, high):
    while divRan(num, low, high)[0] == False:
        num *= divRan(num, low, high)[1]
    return num

#Selects a smaller number than overestimate() that is evenly divisble from a range
def recalibrate(num, low, high):
    for i in range(low, high):
        if num%i == 0:
            if divRan(num/i, low, high)[0] == True:
                num /= i
    return int(num)

#Finds the smallest number that is evenly divisble by a range of numbers
def evenDivRan(low, high):
    return recalibrate(overestimate(2, low, high), low, high)
