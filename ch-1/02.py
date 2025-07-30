# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
def number_of_divide(number: int) -> int:
    if number > 2 : 
        count = 0
        while number >= 2:
            number /= 2 
            count += 1 
        return count 
    else:
        raise ValueError("Number must be greater than 2")
try:
    print(number_of_divide(3))
except Exception as e:
    print(e)
            