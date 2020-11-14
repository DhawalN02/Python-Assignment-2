#!/usr/bin/env python
# coding: utf-8

# Question1 :

# In[1]:


def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = " ")
        print()
    for i in range(n-1,-1,-1):
        for j in range(i):
            print('*',end = " ")
        print()


# In[2]:


pattern(5)


# Question 2:

# In[3]:


def rev(m):
    for i in m:
        print(m[::-1])
        break
    
        


# In[4]:


rev("ineuron")


# In[5]:


rev("Nilesh")


# In[6]:


rev("sudh")


# In[ ]:





# In[ ]:




