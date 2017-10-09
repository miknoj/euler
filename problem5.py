'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
'''
LOWER_BOUND = 1
UPPER_BOUND = 20

# Solution 1
import math

def sieve(upper_bound):
    primes = {x:True for x in range(2, upper_bound)}
    for k in range(2, int(math.sqrt(upper_bound))+1):
        if primes[k]:
            for j in range(k**2, upper_bound, k):
                primes[j] = False
    return [1] + [p for p in primes if primes[p]]

# What is this...?
def factorize(num):
    if num is 1:
        return [1]
    factors = []
    if num <= 0:
        return factors
    primes = sieve(num+1)
    if num in primes:
        return [num, 1]
    primes.remove(1)
    current = num
    while current > 1:
        new = current
        for p in primes:
            if new % p == 0:
                factors.append(p)
                new = new / p
        if current == new:
            break
        current = new
    return factors

def countmap(nums):
    res = dict()
    for x in nums:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    return res

def compute_product(solution_map):
    product = 1
    for k, v in solution_map.items():
        product *= k**v
    return product

if __name__ == '__main__':
    solution_map = countmap(sieve(UPPER_BOUND))
    for num in range(LOWER_BOUND, UPPER_BOUND):
        if num not in solution_map:
            factors = countmap(factorize(num))
            for p in factors:
                if factors[p] > solution_map[p]:
                    solution_map[p] = factors[p]

    solution = compute_product(solution_map)
    print('The answer is {}'.format(solution))