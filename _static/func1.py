from math import sqrt

def rms(a):
    """
    Computes the root mean square of *a*, which is a numpy array. The
    result is a double constant.
    """
    return sqrt((a**2).mean())
