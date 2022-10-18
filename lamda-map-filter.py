import math

lenth = lambda pi, r : 2*pi*r
print(lenth(math.pi,10))

kvadrat = lambda x, y : x ** y
print(kvadrat(3, 2))

def degree(n):
    return lambda x : x**n

kvadrat = degree(2)
kub = degree(3)
print(kvadrat(16))
print(kub(2))

from math import sqrt

numbers = list(range(11))
roots = list(map(sqrt,numbers))
print(roots)

def degree2(x):
    """A function that returns the square of a given number"""
    return x*x
print(list(map(degree2,numbers)))

kvadratlar = list(map(lambda x:x*x, numbers))
print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

import random as r

numbers = r.sample(range(100),10)
print(numbers)
def even_number(x):
    """A function that returns TRUE if x is even, FALSE if not"""
    return x%2==0

even_number = list(filter(even_number,numbers))
print(even_number)

even_number = list(filter(lambda x: x%2==0,numbers))
print(even_number)

fruits = ['apple', 'banana', 'burito', 'grape', 'avacado']
letter = 'a'
fruits_a = list(filter(lambda fruit:fruit.startswith(letter),fruits))
print(fruits_a)

fruits2 = list(filter(lambda fruit:len(fruit)<8,fruits))
print(fruits2)

# Homework
import math

number = lambda x: x*10
print(number(9))

number = lambda x,y: x*y
print(number(2,25))

from random import sample

x = list(range(0,1000))
y = sample(x,k=10)
print(y)

from math import sqrt

kvadratlar = list(map(lambda n: sqrt(n), y)) 
print(kvadratlar)

odd_numbers = list(filter(lambda n: n%2,y))
print(odd_numbers)


def prime(x):
    if x % 2 == 0 or x < 2:
        return False  
    if x == 2 or x == 3:
        return True 
    for z in range(3, x, 2):
        if x % z == 0:
            return False
    return True

prime_numbers = list(filter(prime, range(100)))
print(prime_numbers)
