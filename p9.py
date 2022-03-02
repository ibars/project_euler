'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

result = 0

for i in range(1000,1,-1):
   for j in range(1000,1,-1):
      if (i + j + math.sqrt(i**2+j**2)) == 1000 and i<j:
         result = i*j*(1000 - i - j)
         
print(result)