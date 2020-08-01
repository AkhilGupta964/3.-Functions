import math
import random

print(math)
print(random)

t = random.randint(6,90) # gives random int between 6 and 90 both inclusive
print (t)

m = random.random() # gives random between 0 and 1
print (m)

p = [1,2,3]
u = random.choice(p)
print (u)

def print_l():
    print ('ff')

print_l()

def print_twice(a):
    print(a*2)
    print(a*3)
# print is not return (no variable)

print_twice('po')

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)

def thing(arg):
    print(arg)

thing('There you are')

def stuff():
    print('Hello')
    return # if print('world') here then print that also
    print('World')

stuff()

hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
h = float(hrs)
r = float(rph)

# Grading Tool Quiz

def computepay(h,r):
    if h<=40:
	   	bc = h*r
    else:
        bc = 1.5*h*r -20*r
    return bc

bc = computepay(h,r)
print("Pay",bc)

# write code for fibonacci to a certain boundary

def fibo(ar,a=1,b=1,c=0): # default argument value
    try:
        arg = int(ar)
    except:
        print('Enter an integer')
        exit()
    #a,b,c = 1,1,0
    print (a,b, end =' ') # so that code not go in next line
    while (a+b) < arg :
        c = a + b
        a = b
        b = c
        print (c , end=' ')

ar1 = input ('Enter a num:')
fibo (ar1) # start with 1 and 1
ar2 = input ('\nEnter a num:')
fibo (ar2,2,3) # start with 2 and 3 (which are positional arguments)
ar3 = input ('\nEnter a num:')
fibo (ar3,b=3,a=2) # start with 2 and 3 (which now are keword arguments)
# positional arguments cannot come after keyword arguments
# if you want only positional args then put ', /' after args
# if you want only keyword args then put '*, ' before args
#Example - all keyword args

def fibo(*, ar,a=1,b=1,c=0): # default argument value
    try:
        arg = int(ar)
    except:
        print('Enter an integer')
    #a,b,c = 1,1,0
    print (a,b, end =' ')
    while (a+b) < arg :
        c = a + b
        a = b
        b = c
        print (c , end=' ')

ar1 = input ('\nEnter a num:')
fibo (ar = ar1) # start with 1 and 1
ar2 = input ('\nEnter a num:')
fibo (ar = ar2,a = 2,b = 3) # start with 2 and 3 (which are keyword arguments)

# Example - mixed args

def fibo(ar, *, a=1, b=1, c=0): # default argument value
    try:
        arg = int(ar)
    except:
        print('Enter an integer')
    #a,b,c = 1,1,0
    print (a,b, end =' ')
    while (a+b) < arg :
        c = a + b
        a = b
        b = c
        print (c , end=' ')

ar1 = input ('\nEnter a num:')
fibo (ar1) # start with 1 and 1
ar2 = input ('\nEnter a num:')
fibo (ar2,a = 2,b = 3) # start with 2 and 3 (which are keyword arguments)

# Example - Only positional arguments

def fibo(ar, a=1, b=1, c=0, /): # default argument value
    try:
        arg = int(ar)
    except:
        print('Enter an integer')
    #a,b,c = 1,1,0
    print (a,b, end =' ')
    while (a+b) < arg :
        c = a + b
        a = b
        b = c
        print (c , end=' ')

ar1 = input ('\nEnter a num:')
fibo (ar1) # start with 1 and 1
ar2 = input ('\nEnter a num:')
fibo (ar2,2,3) # start with 2 and 3 (which are positional arguments)
