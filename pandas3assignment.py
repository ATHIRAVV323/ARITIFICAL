#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:



#Datasets
#1. https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv

#2. https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv


# In[3]:


#Q1. Get the Metadata from the above files.


# In[4]:



#1. https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv
df=pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df.head()


# In[6]:


#2. https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv

df1=pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head()


# In[7]:


#1
print("Metadata for data-text") 
df.info()


# In[9]:


#2datset

print("Metadata for berlin_weather_oldest ")  
df1.info()


# In[13]:


#Q2. Get the row names from the above files.


print("row name for first dataset :")
df.index.values


# In[15]:


print("row name for seconf dataset :")
df1.index.values


# In[17]:


#Q3. Change the column name from any of the above file and store the changes made permanently.

df.rename(columns={"Comments":"Comment"},inplace=True)  
df.head()


# In[18]:


#Q4. Change the names of multiple columns.

df.rename(columns={"Indicator":"INDICATOR","WHO region":"WHO Region"},inplace=True) 
df.head(2)


# In[20]:


#Q5. Arrange values of a particular column in ascending order.

df.sort_values('Numeric').head(5)


# In[21]:


#Q6. Arrange multiple column values in ascending order.

df[0:5].sort_values(['Year','INDICATOR','Country']).head()


# In[22]:


#Q7. Make country as the first column of the dataframe.

df.set_index('Country').head()


# In[23]:


#Q8. Get the column array using a variable

import numpy as np
np.array(df[['Numeric']],dtype=np.int)


# In[24]:


#Q9. Get the subset rows 11, 24, 37

df.loc[[11,24,37]]


# In[25]:


#Q10Get the subset rows excluding 5, 12, 23, and 56

df.drop([5,12,23,56])[0:56]


# In[26]:


#Q11.find rows with NaN values


df.isnull()


# In[27]:


#q12. show rows from dataset 1 country = india with high income

c=df[df['Country']=='India']    #indian details
c


# In[28]:


try:
    df[df['Country']=='India'] & df[df['World Bank income group']=='High-income']
except:
    df[df['Country']=='India'].max()

df[df['Country']=='India'].max()  


# In[ ]:




