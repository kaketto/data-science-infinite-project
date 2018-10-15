#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
filename = './google-play-store-apps/googleplaystore.csv'
df = pd.read_csv(filename)
print(df.head()) #print head


# In[2]:


print(df.dtypes)


# In[4]:


df2 = df.copy()


# In[5]:


print(df2.iloc[10472])


# In[6]:


df2.iloc[10472, 2:] = df2.iloc[10472, 1:].shift(1) #data in wrong columns, shift to right
print(df2.iloc[10472])


# In[8]:


df2.iat[10472, 1] = 'Lifestyle' #including missing data for Category
print(df2.iloc[10472])


# In[12]:


df2['Reviews'] = pd.to_numeric(df2['Reviews'])
print(df2.loc[df2['Reviews'].min()])


# In[13]:


print(df2.loc[df2['Reviews'].idxmin()])


# In[19]:


print(df2[df2['Reviews'] == 0]) #filter apps having 0 reviews


# In[24]:


df2.drop_duplicates(keep='first', inplace=True) #remove duplicates


# In[27]:


print(df2.describe())


# In[31]:


print(df2.dtypes)


# In[32]:


df2['Rating'] = pd.to_numeric(df2['Rating']) 
print(df2.dtypes)


# In[33]:


print(df2.describe())


# In[34]:


print(df2.loc[:, 'Rating'].median())


# In[35]:


print(df2.loc[:, 'Rating'].mode())




# In[38]:


df2['Size'] = df2['Size'].replace(r'[mM]', '')



# In[40]:


print(df2.loc[0])




# In[42]:


df2['Size'] = df2['Size'].str.replace(r'[mM]', '')
df2['Size'] = pd.to_numeric(df2['Size'], errors='coerce') 
print(df2.loc[0])


# In[43]:


print(df2.describe())


# In[44]:


print(df2.loc[:, 'Size'].median())
print(df2.loc[:, 'Size'].mode())


# In[51]:


print(df2.groupby(df2['Genres']).count().sort_values('App', ascending=False)[:3])


# In[55]:


df2['Last Updated Readable'] = pd.to_datetime(df2['Last Updated'], errors='coerce')


# In[57]:


print(df2.columns)


# In[58]:


print(df2[['Last Updated', 'Last Updated Readable']])


# In[60]:


df2.to_csv('googleplaystore_updated.csv')


# In[61]:


df2[::-1].to_csv('googleplaystore_reversed.csv')






