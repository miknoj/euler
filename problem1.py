'''
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Simple and clear. Short enough.

if __name__ == '__main__':
    sum = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    print('The answer is {}'.format(sum))