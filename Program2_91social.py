
# coding: utf-8

# In[26]:


print('Program 2')
from datetime import datetime


# In[ ]:


string1 = input('please enter your first date in format YYYY/MM/DD')


# In[28]:


print(type(string1))


# In[29]:


string2 = input('please enter your second date in format YYYY/MM/DD')


# In[30]:


print(type(string2))


# In[35]:


date1 = datetime.strptime(string1,"%Y/%m/%d")


# In[36]:


date2 = datetime.strptime(string2,"%Y/%m/%d")


# In[37]:


diff = date2 - date1


# In[38]:


print("Number of days between the two dates:",abs(diff.days))

