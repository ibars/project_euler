"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
primes = []

def is_prime(n):
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

i = 1
while(len(primes) < 10001):
   i += 1
   if is_prime(i):
      primes.append(i)
   
print(primes[-1])
