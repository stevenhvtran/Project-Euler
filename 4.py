#Euler problem 4
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#Determines if number n is a palindrome
def isPal(n):
    nDigits = [int(i) for i in str(n)]
    for i in range(0, len(nDigits)):
        if nDigits[i] != nDigits[-1-i]:
            return False
    return True

highestPal = 1
for i in range(100,999):
    for j in range(100,999):
        prod = i * j
        if isPal(prod) == True and prod > highestPal:
            highestPal = prod
            print(prod)
