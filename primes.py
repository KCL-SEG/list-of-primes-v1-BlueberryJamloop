"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math
def isPrime(number):
    for x in range(1, math.ceil(math.sqrt(number))):
        if number % x == 0:
            return False
    return True
        
        
        

def primes(number_of_primes):
    listOfPrimes = []
    
    while len(listOfPrimes) < number_of_primes:
        number = 0
        if isPrime(number):
            listOfPrimes.append(number)
        number += 1
    print(listOfPrimes)
    return list


