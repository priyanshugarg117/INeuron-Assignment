#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[12]:


def factorial_rec(num):
    fact = 1
    if num < 0:
        print("factorial doesnot exist for negative number")
    elif num == 1:
        return num
    else:
        return num*factorial_rec(num-1)


# In[14]:


factorial_rec(6)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')


# In[17]:


num = int(input("Enter number for multiplication table"))
for i in range(1,11):
    print(num , "X" , i , "is", num*i)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')


# In[26]:


num = int(input("Enter number of elements in fib series: "))
a  = 1
b = 1

if num ==1:
    print(a)
elif num == 2:
    print(a,b)
else:
    print(a)
    print(b)
    for i in range(1,num-1):
        
        a,b = b, a+b
        print(b)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[31]:


num = int(input("Please enter a number: "))
sum = 0
num_arm = num
unit = 0
digit = len(str(num))
while num != 0:
    unit = num%10
    sum = sum + pow(unit,digit)
    num = num//10
if sum == num_arm:
    print("number is armstrong")
else:
    print("number is not armstrong")
    


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')


# In[4]:



lower = int(input("Enter lower limit: ")) 
upper = int(input("Enter upper limit: "))
print("The armstrong numbers are: ")    

for number in range(lower, upper + 1):
    order = len(str(number))
    #Computes sum of nth power   
    sum_pow = 0

    temp = number
    while temp:
        temp,digit = divmod(temp,10)
        sum_pow+=digit ** order      
    if number == sum_pow:
        print(number)


        


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# In[2]:


num = int(input("please enter number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print("Sum of First {0} Natural Numbers are {1}".format(num, sum))


# In[ ]:




