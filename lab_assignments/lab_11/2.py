# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
# even number last bit = zero 

def is_even(k: int):
    """Return True if k is even else False """
    if not isinstance(k , int): # checking the type of k 
        raise TypeError("k must be int type")
    # handling negative numbers 
    if k < 0 :
        k = abs(k) # convert it in to positive integer 
    while k > 1 :
        k -= 2  # decreasing value of k by 2 till not equal to 1 or zero : 1-> add , 0 -> even 
    return k == 0 

# pythonic loop function 
def is_even_pythonic(k: int):
    """Return True if k is even else False"""
    if not isinstance(k , int): # checking the type of k 
        raise TypeError("k must be int type")
    if k < 0: # handling negative values
        k = abs(k)
    for i in range(0 , k+1 , 2):    
        if i == k :
            return True 
    return False 

try:
    print(is_even_pythonic(6))
except Exception as e:
    print(e)