
# coding: utf-8

# In[2]:


import logging
def get_logger(name):
    log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        filename='test2.log',
                        filemode='w')
    return logging.getLogger(name)


# In[3]:


with open('C:\\Users\\ANMOL S\\Test_log.log') as f:
    lines = f.readlines()
for line in lines:
    logger = get_logger('test')
    logger.info(line)

