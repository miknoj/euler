'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

TARGET = 1000

# Solution 1 - a very quick and dirty solution. Might fail due to floating
# point errors.

import math

def pythagorean_c(a, b):
    return math.sqrt(a**2 + b**2)

if __name__ == '__main__':
    found = False
    for a in range(1, TARGET):
        for b in range(a+1, TARGET):
            c = pythagorean_c(a, b)
            if a+b+c == TARGET:
                found = True
            if a+b+c >= TARGET:
                break
        if found:
            break

    if found:
        print('The answer is {}'.format(a*b*c))
    else:
        print('There are no Pythagorean triplets that sum up to ' \
            + '{} in the set of natural numbers'.format(TARGET))

