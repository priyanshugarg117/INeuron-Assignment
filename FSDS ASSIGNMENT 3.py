#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Write a Python Program to Check if a Number is Positive, Negative or Zero');get_ipython().run_line_magic('pinfo', 'Zero')


# In[3]:


num = int(input("Enter number: "))
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")


# Write a Python Program to Check if a Number is Odd or Even?

# In[8]:


num = int(input("Enter number: "))
if num == 0:
    print("Number is zero")
elif num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')


# In[13]:


year = int(input("please enter year: "))
if len(str(year))>=5:
    print("please enter correct year")
else:
    if year%400 ==0 or (year%4==0 and year%100!=0) :
        print("Year {0} is a leap year".format(year))
    else:
        print("Year {0} is not a leap year".format(year))


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[13]:


num = int(input("Enter number: "))
flag = 0
for i in range(2,num):
    if num%i == 0:
        flag = flag+1
if flag == 0:
    print("Number is Prime")
else:
    print("Number is not prime")


# In[ ]:


Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[6]:


a = 1
b = 10000
l1 = []
for i in range(a,b):
    flag = 0
    if i ==1 or i ==2:
        l1.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                flag = flag +1
        if flag ==0:
            l1.append(i)
print(l1)
                
    


# In[ ]:




