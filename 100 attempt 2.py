import numpy as np
import decimal

def blues(m):
    return (np.sqrt(decimal.Decimal(4)-decimal.Decimal(8)*(decimal.Decimal(m)-decimal.Decimal(m)**decimal.Decimal(2)))+decimal.Decimal(2))/decimal.Decimal(4)

def nextDB(m):
    while blues(decimal.Decimal(m)) != int(blues(m)):
        m += 1
    print(m)

def blues2(n):
    return (np.sqrt(decimal.Decimal(1)-decimal.Decimal(4)*(decimal.Decimal(2)*decimal.Decimal(n)-decimal.Decimal(2)*(decimal.Decimal(n)**decimal.Decimal(2))))+decimal.Decimal(1))/decimal.Decimal(2)

def nextDB2(n):
    while blues2(n) != int(blues2(n)) or blues2(n) < 10**12 :
        n += 1
    print(blues2(n))
    print(n)



