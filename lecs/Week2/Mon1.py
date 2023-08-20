"""Our first python source file."""

from operator import floordiv, mod
def divide_exact(n, d):
    """Return the quotient and remainder of dividing N by D.
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """return the absolute value of x"""
    if x < 0:
        return -x
    elif x >= 0:
        return x
    
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i