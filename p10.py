'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math

primesSum = 0

def isPrime(n):
   if n <= 3:
      return n > 1
   if n % 2 == 0 or n % 3 == 0:
      return False
   i = 5
   while i ** 2 <= n:
      if n % i == 0 or n % (i + 2) == 0:
         return False
      i += 6
   return True

for i in range(2000000):
   if isPrime(i):
      primesSum += i
print(primesSum)
      
