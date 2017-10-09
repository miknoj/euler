'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
'''

TARGET_PRIME_COUNT = 10001

# Solution 1 - A very brute forced approach.
from problem5 import sieve

if __name__ == '__main__':
    current_primes = []
    prime_count = 0
    upper_bound = 100 # A random start number.

    while prime_count < TARGET_PRIME_COUNT:
        current_primes = sieve(upper_bound)
        prime_count = len(current_primes)
        upper_bound += prime_count
        
    print('The answer is {}'.format(current_primes[TARGET_PRIME_COUNT]))