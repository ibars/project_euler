'''
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

f = open('data/p11.txt', 'r')

prod_size = 4

data = []
for line in f:
   line.replace(' ', ',')
   line = list(map(int, line.split()))
   data.append(line) 
   
f.close()

grid_s = len(data)
max_prod = 0

for i in range(grid_s):
   for j in range(grid_s):
      
      if i >= prod_size - 1 and j <= grid_s - prod_size:
         product = 1
         for k in range(prod_size):
            product *= data[j+k][i-k]
         if product > max_prod:
            max_prod = product
      
      if i <= grid_s - prod_size:
         product = 1
         for k in range(prod_size):
            product *= data[j][i+k]
         if product > max_prod:
            max_prod = product
            
      if j <= grid_s - prod_size:
         product = 1
         for k in range(prod_size):
            product *= data[j+k][i]
         if product > max_prod:
            max_prod = product
      
      if i <= grid_s - prod_size and j <= grid_s - prod_size:
         product = 1
         for k in range(prod_size):
            product *= data[j+k][i+k]
         if product > max_prod:
            max_prod = product

print(max_prod)
