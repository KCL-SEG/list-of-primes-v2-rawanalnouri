"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes > 0:
        list = []
        num = 0
        while len(list) < number_of_primes:
            if isPrime(num):
                list.append(num)
            num += 1
        return list
    else:
        raise ValueError("Input must be greater than 0.")

def isPrime(num):
    flag = True
    if num <= 1:
        flag = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag
