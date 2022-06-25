#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to print &quot;Hello Python&quot;?

# In[1]:


print("Hello Python")


# In[ ]:


Write a Python program to do arithmetical operations addition and division.?


# In[2]:


first_num = int(input("Enter First number: "))
sec_num = int(input("Enter Second number: "))
if sec_num == 0:
    print("Please enter non-zero number")
else:
    add = first_num + sec_num
    div = first_num/sec_num
    print("Addition of numbers {0} and {1} is {2}".format(first_num, sec_num, add))
    print("Division of number {0} by {1} is {2}".format(first_num, sec_num, div))


# Write a Python program to find the area of a triangle?

# In[3]:


height = int(input("Enter Heigh of triangle: "))
base = int(input("Enter base length of triangle: "))
area = (height*base)/2
print("Area of triangle when height is {0} and base is {1} is {2} units".format(height, base, area))


# Write a Python program to swap two variables?

# In[4]:


#method 1:
first_num = int(input("Enter First number: "))
sec_num = int(input("Enter Second number: "))
swap_var = 0
swap_var = first_num
first_num = sec_num
sec_num = swap_var
print("Now first numbers becomes {0} and second number becomes {1}".format(first_num,sec_num))


# In[5]:


#method 2:
first_num = int(input("Enter First number: "))
sec_num = int(input("Enter Second number: "))
first_num, sec_num = sec_num, first_num
print("Now first numbers becomes {0} and second number becomes {1}".format(first_num,sec_num))


# Write a Python program to generate a random number?

# In[10]:


import random
a = random.uniform(1,100)
print(int(a))


# In[ ]:




