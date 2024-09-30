# -*- coding: utf-8 -*-
"""recursion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MM_3nnlMpPxOmJGKLQppDyI4H1pk5SmI
"""

#RECURSION
#Write a factorial function by using recursion
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
result = factorial(5)
print(result)

#Write a funtion to print Fibbonacci series upto 6 using recursion.
def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
result=fibo(6)
print(result)