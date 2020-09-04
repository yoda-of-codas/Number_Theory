#!/usr/bin/python
#Code By Bakel Begededum
"""The plight of this code is to evaluate permutation and combination of numbers """

#Function to evaluate factorials as this is the basis

def f(x):
   
    f = 1
    while x>1:
        f =f* x*(x-1)
        x = x-2
    num = [int(y) for y in str(f)]
    return f

#Function to evaluate Combination
def C(n,r):
    comb = int(f(n)/(f(n-r)*f(r)))
    return (str(n)+' Combination '+str(r)+' = '+str(comb))

#Function to evaluate Permutation
def P(n,r):
    Perm = int(f(n)/f(n-r))
    return (str(n)+' Permutation '+str(r)+' = '+str(Perm))

def tryagain():
    print('Try Again? y/n')
    tryy = str(input())
    tryy = tryy.lower();
    if tryy  == 'y' or tryy == 'yes':
        Main()
    else:
        print ('Thank you for using me')
    

#Main Function to evaluate choice of user...curtsey C++
def Main():
    print('For Permutation enter P\nFor Combination enter C')
    try:
        inp = str(input())
        if inp == 'C' or inp=='c':
            print ('Combination it is\nIn the format nCr, Enter your data')
            n = int(input('Enter n: '))
            if n <= 0:
                print('n cannot be zero or negative')
                Main()
            else:
                r = int(input('Enter r: '))
                print(C(n,r))
                tryagain()
            
        elif inp =='P' or inp=='p':
            print ('Permutation it is\nIn the format nPr, Enter your data')
            n = int(input('Enter n: '))
            if n<=0:
                print('n cannot be negative or zero')
                Main()
            else:    
                r = int(input('Enter r: '))
                print(P(n,r))
                tryagain()
        else:
            print ('Invalid Input')
            Main()
    except:
        print ('invalid Input')
        Main()
#End of definition of function... Let the fun begin
if __name__ == '__main__':
    Main()
