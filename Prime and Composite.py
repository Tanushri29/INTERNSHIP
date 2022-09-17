#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Program to find whether a number is Prime or Composite

n= int(input("Enter any number:"))
if(n==0 or n==1):
    print("Number is neither Prime nor Composite")
elif n>1:
    for i in range(2,n):
         if(n % i == 0):
            print(n,"is composite number")
            break
    else:
        print(n,"is prime number")
else:
     print("Please enter positive number only")
        

