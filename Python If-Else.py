'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

'''
import math
import os
import random
import re
import sys



n=input()
o=int(n) % 2

if o==0:
    if int(n)>20:
        print('Not Weird')
    elif int(n)>=2 and int(n)<=5:
        print('Not Weird')
    elif int(n)>=6 and int(n)<=20:
        print('Weird')
else:
  print('Weird')
