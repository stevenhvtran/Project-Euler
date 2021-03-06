#Euler problem 2
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
#increments by fibonacci sequence
def fib(a, b):
    return([b, a+b])

#checks if the second number is even
def evenFib(a, b):
    if b%2 == 0:
        return b
    else:
        return 0

#initial conditions
num = [1, 2]
total = 0

#adds the even numbers on to total while the larger number is below 4 million
while num[1] < 4000000:
    total += int(evenFib(num[0], num[1]))
    num = fib(num[0], num[1])
    
print(total)
    
