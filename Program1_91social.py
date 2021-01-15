
# coding: utf-8

# In[16]:


print("Program 1")
count = 0
with open("E:\Telly.txt") as f: 
    Lines = f.readlines() #storing in List
    for line in Lines: 
        count += 1
        print("Line{}: {}".format(count, line.strip())) 
print("Total number of lines in text file is:",count)

