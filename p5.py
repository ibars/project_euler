"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

result = 0
step = 0

def is_divisible_by_all(num):
   for i in range(1,20):
      if num % i != 0:
         return False
   return True

#The result has to be divisible by all prime numbers below 20, 
#this product will be the iteration step 

while(result == 0):
   step += 19*17*13*11*7*5*3*2
   if is_divisible_by_all(step):
      result = step
      print(step)