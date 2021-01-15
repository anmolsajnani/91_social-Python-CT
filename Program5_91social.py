
# coding: utf-8

# In[47]:


print('Program 5')
#Version1

num_of_words = 0
with open('E:\Telly.txt','r') as f:
    for line in f:
        words = line.split(" ")
        num_words += len(words)
print('Number of words in file:',num_of_words)

#-----------------------------------------------------------------------------------------------
#Version2

import re
num_of_words = 0
with open('E:\Telly.txt','r') as f:
    lines = f.readlines()
    for line1 in lines:
        line1 = re.sub(r"""
                        [,.-;!@#?&]+
                        \ *\n
                        """," ",line1)
        words = line1.split(" ")
        num_of_words += len(words)
print('Number of words in file:',num_of_words)

