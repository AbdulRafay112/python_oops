# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

import itertools
chars = ['c' , 'a' , 't' , 'd' , 'o']
permuataions = itertools.permutations(chars)
for p in permuataions:
    print(''.join(p))
