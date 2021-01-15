
# coding: utf-8

# In[11]:


print('Program 4')
org_list = [{'make':'Nokia','model':'216','color':'Black',},
            {'make':'Mi Max','model':'2','color':'Gold'},
            {'make':'Samsung','model':'7','color':'Blue'}]


# In[12]:


print(org_list)


# In[13]:


Sorted_list = sorted(org_list, key = lambda i:i['color'])


# In[14]:


print(Sorted_list)

