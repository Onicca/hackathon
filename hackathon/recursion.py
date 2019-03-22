def sum_array(array):

    '''Return sum of all items in array'''
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    '''Return word in reverse'''

    for item in word:
        if len(word) == 1:
            return word
        else:
            return word[-1] + reverse(word[0:-1])
