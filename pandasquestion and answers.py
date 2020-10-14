#!/usr/bin/env python
# coding: utf-8

# In[2]:


df4=pd.read_csv('https://raw.githubusercontent.com/akhil12028/Bank-Marketing-data-set-analysis/master/bank-additional-full.csv',sep=';')
df4


# In[6]:


#1:read data from below ur
#https://raw.githubusercontent.com/akhil12028/Bank-Marketing-data-set-analysis/master/bank-additional-full.csv


import pandas as pd
df4=pd.read_csv('https://raw.githubusercontent.com/akhil12028/Bank-Marketing-data-set-analysis/master/bank-additional-full.csv',sep=';')
df4


# In[9]:


#2 print first 5 rows
df4=pd.read_csv('https://raw.githubusercontent.com/akhil12028/Bank-Marketing-data-set-analysis/master/bank-additional-full.csv',sep=';')
df4[:5]


# In[11]:


#3: print last 2 rows
df4.tail(2)


# In[15]:


#4:change same column names
change=df4.rename(columns={'age':'Age'})
change


# In[20]:


#5: select a column and print its type
type=df4.dtypes['age']
type


# In[22]:


#6. print datatype of dataset
type=df4.dtypes
type


# In[24]:


#7. check any data dats is null

check=pd.isnull(df4)
check


# In[25]:


#8. skip random rows like 20,21, and 45
df4 = pd.read_csv('https://raw.githubusercontent.com/akhil12028/Bank-Marketing-data-set-analysis/master/bank-additional-full.csv',sep=';', 
                  skiprows = [20, 21, 45]) 
df4

