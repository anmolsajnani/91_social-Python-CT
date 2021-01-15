
# coding: utf-8

# In[13]:


print('Program 3')
import json


# In[14]:


dict = {
  "name": "Anmol",
  "age": 23,
  "city": "Mumbai",
  "qualification": "B.Tech in Computer Engineering",
  "5": 6,
  "1": 7
}


# In[15]:


print(dict)


# In[16]:


print('Output Converted to JSON data is as follows')
print(json.dumps(dict, sort_keys = True, indent = 4))

