'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Solution 1
from itertools import combinations as combo

def is_palindrome(num):
    num_as_str = str(num)
    for i in range(int(len(num_as_str)/2)):
        if num_as_str[i] != num_as_str[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    LOWER_END = 100
    UPPER_END = 999

    max_palindrome = 0
    for a, b in combo(range(LOWER_END, UPPER_END), 2):
        product = a * b
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

    print('The answer is {}'.format(max_palindrome))