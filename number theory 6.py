#!/usr/bin/python
import math

ans = []
for i in range(1000,10000):
   num = str(i)
   #check to ensure the number format aabb is met
   if num[0] == num[1] and num[2] == num[3]:
      print('testing',i)
      #check to see make sure the number is a perfect square.
      #the normal root will be equal to the root rounded to any number in this case 5
      if math.sqrt(i)==round(math.sqrt(i),5):
         ans.append(i)
print('The number aabb which is a perfect square is' ,ans)
      
