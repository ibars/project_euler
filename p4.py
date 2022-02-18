"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
result = 0

def is_palindrome(number):
   l_num = list(str(number))
   if(l_num == l_num[::-1]):
      return True
   return False

for i in range(999,1,-1):
   for j in range(i,1,-1):
      if is_palindrome(i*j) and i*j > result:
         result = i*j

print(result)