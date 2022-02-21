"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product in p8.txt. What is the value of this product?
"""

f = open('data/p8.txt','r')

data = []
for line in f:
   for char in line:
      if char != "\n":
         data.append(int(char))
         
f.close()

result = 0

for i in range(len(data) - 13):
   tmp = 1
   for j in range(13):
      tmp *= data[i + j]
   if tmp > result:
      result = tmp
   
print(result)
