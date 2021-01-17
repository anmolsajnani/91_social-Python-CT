
# coding: utf-8

# In[12]:


import array
A = array.array('i',[10,20,30,40,15,25,35,45])


# In[13]:


print (A)


# In[14]:


B = A.tobytes()


# In[15]:


print(B)


# In[16]:


import binascii
print(binascii.hexlify(B))

