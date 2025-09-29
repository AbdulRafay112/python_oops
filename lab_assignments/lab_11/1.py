# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n , m):
    """Return True if n is a multiple of m , else False
    Raises type error if inputs are not integers.
    """
    if not isinstance(n , int) or not isinstance(m , int):
        raise TypeError("n or m must must be integer type")
    if m == 0 :
        raise ValueError("m can not be Zero")
    return n%m == 0  
try:
    print(is_multiple(6,3))
    print(is_multiple("10" , 2))
    print(is_multiple(6 , 0))
except Exception as e:
    print(e)