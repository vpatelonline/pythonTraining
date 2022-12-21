#Exapmple 1

def create_cube(n):
   # result=[]
   # for x in range (n):
   #     result.append(x**3)
   # return result

   for x in range (n):
        yield (x**3)

for x in create_cube(10):
    print (x)


#Exapmple 2

def fibo(n):
    a=1
    b=1

    #output=[]
    #for i in range(n):
    #    output.append(a)
    #    a,b=b,a+b
    #return output

    for i in range(n):
        yield a
        a,b=b,a+b

for num in fibo(10):
    print(num)



#Exapmple 3

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print (number)

g = simple_gen()
print(g)



#Exapmple 4

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,100,5):
    print(num)