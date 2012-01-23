from math import sqrt

def rms(a):
    """
    Computes the root mean square of *a*, which is a numpy array. The
    result is a double constant.
    """
    return sqrt((a**2).mean())

def cmc(a):
    """
    Computes the cubic root mean cube of *a*, which is a numpy array.
    The result is a double constant.
    """
    return ((a**3).mean())**(1.0/3.0)

def nmn(a,n):
    """
    Computes the nth root mean nth power of *a*, which is a numpy array.
    The result is a double constant.
    """
    return ((a**n).mean())**(1/float(n))
