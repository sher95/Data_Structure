from array import *
import numpy as np
from functools import reduce

# All values should be in one type
# Python is single array only
"""
value = array('i', [12, 23, 34, 34, 45])
value.reverse()

print(value.buffer_info())  # this function give address and length of array

arr = array('i', [])

n = int(input("Enter length "))

for i in range(n):
    x = int(input("enter values "))
    arr.append(x)

print(arr)

val = int(input("search "))

k = 0
for a in arr:
    if a == val:
        print("found", k)
        break
    k += 1
"""
"""
nparr = np.array([[12, 32, 34, 43, 21, 11], [32, 21, 1, 5, 65, 52]])

print(nparr, nparr.dtype)
"""
"""
def fib(m):

    a = 0
    b = 1
    for i in range(2, m):
        c = a + b
        a = b
        b = c
        print(c)

fib(10)
"""
# Recursion
"""import sys

sys.setrecursionlimit(2000)
#print(sys.getrecursionlimit())
i = 0


def greet():
    global i
    i += 1
    print("hello", i)
    greet()


greet()"""

# lambda
"""
lt = [2, 3, 5, 1, 6, 9, 4]
even = list(filter(lambda n: n % 2 == 0, lt))

double = list(map(lambda n: n*2, even))

sum = reduce(lambda a, b: a + b, double)
print(even)
print(double)
print(sum)
"""

# Decorator - add extra feature and execute it
"""
def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a>b:
            a,b = b,a
            return func
    return inner

div(2, 3)"""

# OOP
"""
class Person:
    wheel = 4

    def __init__(self, name, model):
        self.name = name
        self.model = model

        print(name, model)

    def config(self):
        a = 2 * self.model
        print("Asus rog 13\n", a)


Person.wheel = 5

com1 = Person('Aser', 15)
com2 = Person("HP", 17)
com1.config()
"""

# Operator overloading
"""
a = '5'
b = 'hello'
exit
#print(a + b)
print(str.__add__(a, b))"""

# Abstract
"""
from abc import ABC, abstractmethod


class Computer:
    @abstractmethod
    def process(self):
        print("threading")"""

# Iterator
"""
nums = [2, 5, 7, 1, 3]

it = iter(nums)

print(it.__next__())
print(it.__next__())
print(next(it))"""

# Generator
"""
def top():
    yield 5


val = top()

print(val.__next__())"""

# multithreading
from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
t1.join()  #join will run til end
t2.join()
print("Bye")  #then will print it
