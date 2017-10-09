'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''
from math import sqrt

THE_TARGET = 600851475143

# Solution 1
def divisors(upper_bound):
    # Only yield odd numbers to cut search space in half.
    for num in range(3, int(sqrt(upper_bound)), 2):
        yield num

def get_upper_prime(target):
    max_prime = 1
    for num in divisors(target):
        if target % num != 0:
            continue
        usda_prime = True
        for divr in divisors(num):
            if num % divr == 0:
                # The number is NOT usda prime!
                usda_prime = False
                break
        if usda_prime: 
            max_prime = num
    return max_prime

if __name__ == '__main__':
    print('The answer is {}'.format(get_upper_prime(THE_TARGET)))