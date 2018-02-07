#Euler problem 100
'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
'''

import numpy

#Checks to see if a number will produce a probabilty of 1/2 if there are that many discs
def doubleBlue(number):
    #Upper and lower bounds for randomisation
    #Change this for lower numbers
    low = int(number*0.69)
    high = int(number*0.71)
    #Denom stays constant
    denominator = number * (number - 1)
    #Eliminates any non factorising denominators
    if denominator%2 != 0:
        return False
    #0.7 is a good starting estimate as 0.7**2 = 0.49
    numeratorGuess = int(number*0.7)
    numerator = numeratorGuess * (numeratorGuess + 1)
    #Counter for guesses
    guesses = 0
    #Does the actual search 
    while numerator/denominator != 0.5 and guesses < 25:
        if numerator/denominator > 1/2:
            high = numeratorGuess 
            numeratorGuess = numpy.random.randint(low, numeratorGuess)
            numerator = numeratorGuess * (numeratorGuess + 1)
            guesses += 1
        else:
            low = numeratorGuess
            numeratorGuess = numpy.random.randint(numeratorGuess, high)
            numerator = numeratorGuess * (numeratorGuess + 1)
            guesses += 1
    if numerator/denominator == 0.5:
        return (numeratorGuess + 1)
    else:
        return False

#Use to confirm number to print string
def Blue(number):
    low = int(number*0.65)
    high = int(number*0.75)
    denominator = number * (number - 1)
    numeratorGuess = int(number*0.7)
    numerator = numeratorGuess * (numeratorGuess + 1)
    guesses = 0
    while numerator/denominator != 0.5 and guesses < 30:
        if numerator/denominator > 1/2:
            high = numeratorGuess 
            numeratorGuess = numpy.random.randint(low, numeratorGuess)
            numerator = numeratorGuess * (numeratorGuess + 1)
            guesses += 1
        else:
            low = numeratorGuess
            numeratorGuess = numpy.random.randint(numeratorGuess, high)
            numerator = numeratorGuess * (numeratorGuess + 1)
            guesses += 1
    return (numeratorGuess + 1)

def nextDB(number):
    while doubleBlue(number) == False:
        number += 1
    print(str(Blue(number)) + ' is the number of blue discs and the total is ' + str(number) + ' discs')

