# -*- coding: utf-8 -*-
"""week3pythonfunction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rVwWq1JICf3OA04ex8alUmNoQ7HQQF79
"""

print("this is my program")

l = [1,2,3,4,5]

len(l)

def test():
    pass

def test1():
  print("this is my very very first fun")

test1()

#test1() + "sudh"

def test2():
  return "this is my fun with return "

test2()

test2() + "sudh"

def test3():
  return 1, 4, "pwskills", 34.56

test3()

a = 1,2,3,4,5

a

a,b,c,d = 1,2,34.56,True

a

b

c

d

test3()

test3()[0]

test3()[1]

test3()[2]

a,b,c,d = test3()

a

b

c

d

def test4():
    a = 3*4 + 5
    return a

type(test4())

def test5(a,b):
    c = a + b
    return c

test5(a,b)

test5(1,3)

test5("sudh" , "kumar")

test5([1,2,3,4] , [4,5,6,7,8])

test5(b = "sudh" , a = "kumar")

l = [1,2,3,4,5,"sudh" , "pwskills" , [1,2,3,34,45]]

#create a function which will take list as a input and give me a final list with all the numeric value
def test6(a):
    n = []
    for i in a :
        if type(i) == int or type(i) == float :
            n.append(i)
    return n

test6(l)

l

def test7(a) :
    n = []
    for i in a :
        if type(i) == list :
            for j in i :
                if type(j) == int or type(j) == float :
                   n.append(j)
        else :
            if type(i) == int or type(i) == float :
              n.append(i)
    return n

test7(l)

l

def test(a,b,c,d,e):
    pass

test(1,2,3,4,5)

#test(1,2,3,4,5,6,7)

def test1(*args):
    return args

test1(2)

test1(1,2,3,4,5,5)

test1("sudh" ,[1,2,3,4,5], (1,2,3,4,5))

def test2(*sudh):
  return sudh

test2(3,4,5,6)

def test3(*args , a):
    return args ,a

#test3(3)

test3(1,2,3,4 ,a="sudh")

def test4(*args):
    l = []
    for i in args:
        if type(i) == list:
            l.append(i)
    return l

test4(1,2,3,[1,2,3,4,4] ,(1,2,3,4,4), "sudh", [4,5,6] ,[6,7,8])

def test5(**kwargs):
    return kwargs

test5()

type(test5())

test5(a = 34, b = 23, c = [1,2,3,4], d = ("sudh", "pwskills"))

def test6(**kwargs):
    for i in kwargs.keys():
        if type(kwargs[i]) == list :
           return i , kwargs[i]

test6(a = 34, b = 23, c = [1,2,3,4], d = ("sudh", "pwskills"))

def test7(*args, **kwargs) :
    return args, kwargs

test7(2,3,4,5,a = 34, b = 98)

## generator function

range(1,10)

for i in range(1,10):
    print(i)

l = [1,2,3,4,4,5,6,7,8,7,"sudh", "pwskills"]

def test1(a) :
    n = []
    for i in a :
        if type(i) == int :
            n.append(i)
    return n

test1(l)

#Fibonacci :

  #0,1,1,2,3,5,8,13,21,

def test_fib(n) :
  a,b = 0,1
  for i in range(n):
      yield a
      a,b = b, a+b

test_fib(10)

for i in test_fib(10) :
    print(i)

## lambda function

n = 3
p = 2

def test(n,p):
  return n**p

test(3,2)

test(9,4)

a = lambda n,p : n**p

a(3,2)

a(9,4)

add = lambda x,y : x+y

add(234,34)

c_to_f = lambda c : (9/5)*c+32

c_to_f(34)

max_two = lambda x,y : x if x>y else y

max_two(4,56)

s = "pwskills"

len_st = lambda s : len(s)

len_st(s)

#map, reduce, filter function

l = [1,2,3,4,45,5]

def test(l):
  l1 = []
  for i in l:
      l1.append(i**2)
  return l1

test(l)

def sq(x):
  return x**2

list(map(sq, l))

map(sq, l)

list(map(lambda x : x**2, l))

list(map(lambda x : x+10, l))

list(map(lambda x : str(x), l))

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

list(map(lambda x,y :x+y, l1, l2))

f = lambda x,y :x+y
list(map(f, l1, l2))

s = "pwskills"

list(map(lambda x : x.upper(), s))

from functools import reduce

l = [1,2,3,4,5,4]

sum(l)

reduce(lambda x, y : x+y, l)

def add(x,y):
    return x+y

reduce(add, l)

#reduce(lambda x, y, z : x+y+z, l)

#reduce(lambda x , y : x+y , [])

reduce(lambda x , y : x+y , [l])

reduce(lambda x , y : x*y , [l])

reduce(lambda x , y : x*y , [l])

reduce(lambda x , y : x if x>y else y, l)

l

list(filter(lambda x : x % 2 == 0 , l))

list(filter(lambda x : x % 2 == 1 , l))

l1 = [-2,4,5,6,-3,-6,-7]

list(filter(lambda x : x < 0, l1))

list(filter(lambda x : x > 0 , l1))

l2 = ["sudh" , "pwskills" , "kumar" , "banglore" , "krish"]

list(filter(lambda x : len(x) < 6 , l2))
