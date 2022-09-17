#!/usr/bin/env python
# coding: utf-8

# In[1]:


str_1= input("Enter the string to check if it is a Palindrome:")
str_1= str_1.casefold()
rev_str = reversed(str_1)
if list (str_1) == list (rev_str):
     print("The string is Palindrome")
else:
     print("The string is not Palindrome")

