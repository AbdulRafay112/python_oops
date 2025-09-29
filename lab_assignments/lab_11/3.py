# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def min_max(data):
    """Return a tuple of maximum and minimum from a sequence of numbers"""
    if len(data) == 0 :
        raise ValueError("data must contain atleast 1 number")
    smallest = largest = data[0]
    for value in data[1:]:
        if value < smallest:
            smallest = value 