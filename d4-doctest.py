def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-1.2)
    1.44
    """

    return x * x

def checkPrime(n):
    """Check is prime number
    >>> checkPrime(7)
    True
    >>> checkPrime(9)
    False
    >>> checkPrime(2)
    True
    """

    return len([x for x in range(1, n + 1) if n % x == 0]) == 2

def makeThisNotCover(n):
    """Check is so chan, le
    >>> makeThisNotCover(2)
    True
    >>> makeThisNotCover(3)
    False
    >>> makeThisNotCover(0)
    False
    """

        
    if n == 0: return False

    if n % 2 == 0:
        return True
    else:
        return False

import doctest
doctest.testmod()