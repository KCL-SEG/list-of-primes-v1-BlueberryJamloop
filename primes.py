"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    for x in range(1, ceil(sqrt(number))):
        if number % x == 0:
            return False
    return True
        
        
        

def primes(number_of_primes):
    listOfPrimes = []
    
    while len(listOfPrimes) < number_of_primes:
        for number in range(1):
            if isPrime(number):
                listOfPrimes.append(number)
    print(listOfPrimes)
    return list


