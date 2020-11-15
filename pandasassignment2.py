#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

df1=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv')
df1.head()


# In[4]:


# 1:Convert the type of the column Year to datetime64

data=pd.to_datetime(df1['Year'])
data.head()


# In[6]:


# 2: Set the Year column as the index of the dataframe¶

df1.set_index('Year').head()


# In[8]:


# 3:Return the first 3 rows of the DataFrame df.
df1.head(3)


# In[10]:


# 4: Select just the 'Murder' and 'Robbery' columns from the DataFrame df and print first 5 rows


s=df1[['Murder','Robbery']]
s.head()


# In[12]:


# 5:Select the data in rows [3, 4, 8] and in columns ['Murder', 'Robbery']

df1.loc[[3,4,8]][['Murder','Robbery']]


# In[14]:


# 6:Select only the rows where the number of murder is greater than 24,000

rows=np.where(df1['Murder']>24000)
rows
df1.iloc[rows]


# In[16]:


# 7:Select the rows the murder is between 20k and 24k (inclusive)

df1.loc[(df1['Murder'] >= 20000) & (df1['Murder'] <= 24000)]


# In[20]:


# 8:Calculate the mean murder for each different year in df.

df1['MeanYear']=df1['Murder']/df1['Total']
df1.head()


# In[21]:


# 9: Sort df first by the values in the 'Murder' in decending order, then by the value in the 'Violent'column in ascending order.


# In[23]:


df1.sort_values('Murder',ascending=False).head()    #Sort df1 first by the values in the 'Murder' in decending order


# In[24]:


df1.sort_values('Violent',ascending=True).head()

