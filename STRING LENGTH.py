#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string=input("Enter the string: ")
str1=list(string)
strlist=[]
for j in str1:
    if j not in strlist:
        strlist.append(j)
        count=0
        for i in range(len(str1)):
            if j==str1[i]:
                count+=1
        print("{},{}".format(j,count))
        

