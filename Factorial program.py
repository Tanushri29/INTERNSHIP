#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Program to find the facorial of a number

n= int(input ("Enter the number for which factorial needs to calculated"))
factorial=1
if n<0:
     print("Factorial does not exist for negative numbers")
elif n==0:
     print("Factorial of the number is 1")
else:
        for i in range (1, n+1):
             factorial= factorial*i
        print("Factorial of the given number is:", factorial)


# In[ ]:




