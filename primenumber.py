def organize(prime):
   ans,j ='',0
   while j < len(prime):
      ans = ans + str(prime[j])+' , '
      if j%9==0 and j !=0:
         ans = ans + '\n'
      j+=1
      
   return ans

def primenumbergen(lower,upper):
   prime=[]
   for num in range(lower,upper+1):
      if num>1:
         for i in range(2,num):
            if (num%i)==0:
               break
         else:
            prime.append(num)
   return prime

   

def primefactors(num):
   prime = primenumbergen(0,num)
   fac = ''
   for p in prime:
      if num%p==0:
         A=True
         while A==True:
            fac = fac+str(p)+' x '
            num = num/p
            if num%p != 0:
               A=False
               
   ans = fac[0:len(fac)-2]   
   return ans

def inputs():
   print('+=+'*17)
   print('| To get prime numbers between two numbers Enter 1 |')
   print('| To get the prime factors of any number Enter 2   |')
   print('+=+'*17)
   i = input('')
   if i =='1':
      lower = int(input('Enter the lower number: '))
      upper = int(input('Enter the upper number: '))
      print(organize(primenumbergen(lower,upper)))
      inputs()
   elif i =='2':
      num = int(input('Enter the number to find the prime factor: '))
      print(primefactors(num))
      inputs()
   else:
      print('Wrong input try again')
      input()
      
       
if __name__ == '__main__':
    inputs()
