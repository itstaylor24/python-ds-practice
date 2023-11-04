def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    for x in range(1, num+1):
        if num % x == 0:
            return x
        

#         In the above program, we are just iterating from 1
#         to the number itself and checking if each number in
#         this range is completely divisible by the given value
#         of 'N'. If it leaves a remainder of 0 then we print
#         the result otherwise check for another value in the range.

# The print statement includes the end keyword as end=' '
# which is just used to print the numbers in the same line.
