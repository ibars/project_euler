"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

p_num = 600851475143

def isPrime(n):
   if n < 2:
      return -1
   if n % 2 == 0 or n % 3 == 0:
      return False
   for i in range(5,int(math.sqrt(n))):
      if n % i == 0:
         return False
   return True

def largestPrime(num):
   num_sqrt = int(math.sqrt(num))
   for i in range(num_sqrt,1,-1):
      if num % i == 0 and isPrime(i):
         return(print(i))

largestPrime(p_num)