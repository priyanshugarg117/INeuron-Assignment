#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[4]:


len_km = float(input("Enter length in KMs: "))
len_miles = len_km*0.621371
print("Length in miles is: ", + round(len_miles,3))


# Write a Python program to convert Celsius to Fahrenheit?

# In[5]:


temp_cel = float(input("Enter temprature in Celcius: "))
temp_feh = (temp_cel*9)/5 + 32
print("temprature in Fahrenheit is: ", + round(temp_feh,3))


# In[ ]:


get_ipython().set_next_input('Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[10]:


import calendar
year = int(input("Enter year in yy format: "))
month = int(input("Enter month in mm format: "))
print(calendar.month(year,month))


# In[ ]:


get_ipython().set_next_input('Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')


# In[22]:


import cmath
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

num1 = -b - cmath.sqrt(b*b-(4*a*c))
num2 = -b + cmath.sqrt(b*b-(4*a*c))
print(cmath.sqrt(b*b-(4*a*c)))
val1 = num1/(2*a)
val2 = num2/(2*a)
print(val1)
print(val2)


# In[ ]:


get_ipython().set_next_input('Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[23]:


first_num = int(input("Enter First number: "))
sec_num = int(input("Enter Second number: "))
first_num, sec_num = sec_num, first_num
print("Now first numbers becomes {0} and second number becomes {1}".format(first_num,sec_num))


# In[ ]:




