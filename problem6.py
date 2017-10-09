'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385.

The square of the sum of the first ten natural numbers is 3025.

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

if __name__ == '__main__':
    # This was simple, at least with Python.
    N = 100
    sum_of_sqs = sum([x**2 for x in range(1,N+1)])
    sq_of_sum = (sum([x for x in range(1,N+1)]))**2

    solution = sq_of_sum - sum_of_sqs
    print('The answer is {}'.format(solution))