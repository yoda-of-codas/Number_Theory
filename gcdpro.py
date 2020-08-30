from math import gcd
import functools

def gcds(nums):
   ans = functools.reduce(gcd,nums)
   print(ans)
   
   
print("To find greatest common divisor")
n = int(input("Enter the amount of numbers: "))
nums = []
for i in range(0,n):
   if i ==0:
      a = int(input("Enter the 1st number: "))
   if i ==1:
      a = int(input("Enter the 2nd number: "))
   if i ==2:
      a = int(input("Enter the 3rd number: "))
   if i>2:
      a = int(input("Enter the "+str(i+1)+"th number: "))
   nums.append(a)

nums.sort()
gcds(nums)
