#!/usr/bin/env python
# coding: utf-8

# Write a Python Program to find sum of array?

# In[4]:


ls = [2,4,6,78,81,65,82]
sum = 0
for i in ls:
    sum = sum + i
print("sum of elments of array is:", sum)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to find largest element in an array');get_ipython().run_line_magic('pinfo', 'array')


# In[3]:


ls = [2,4,6,78,81,65,87,24,91]
temp = 0 
for i in ls:
    if i > temp:
        temp = i
print(temp)


# In[ ]:


get_ipython().set_next_input('Write a Python Program for array rotation');get_ipython().run_line_magic('pinfo', 'rotation')


# In[16]:


#rotate ls by r times by slicing:
ls = [2,4,6,78,81,65,87,24,91]
r = int(input("enter number of rotation required: "))
ls[:] = ls[r:]+ls[0:r]
print(ls)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Split the array and add the first part to the end');get_ipython().run_line_magic('pinfo', 'end')


# In[20]:


ls = [2,4,6,78,81,65,87,24,91]
if len(ls)%2==0:
    r=int(len(ls)/2)
    #print(r)
else:
    r = int((len(ls)+1)/2)
    #print(r)
ls[:] = ls[r:]+ls[0:r]
print(ls)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to check if given array is Monotonic');get_ipython().run_line_magic('pinfo', 'Monotonic')

