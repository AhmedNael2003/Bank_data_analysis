#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns                       
import matplotlib.pyplot as plt    
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df = pd.read_csv("Churn Modeling.csv")
df             


# In[3]:


df = df.drop(["Surname", "RowNumber"], axis=1)
print(df.head(5))


# In[4]:


df =pd.get_dummies(df,drop_first=True)


# In[5]:


sns.boxplot(x=df['Balance'])


# In[6]:


sns.boxplot(x=df['CustomerId'])


# In[7]:


sns.boxplot(x=df['CreditScore'])


# In[8]:


sns.boxplot(x=df['Age'])


# In[9]:


sns.boxplot(x=df['EstimatedSalary'])


# In[202]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Age'], df['CreditScore'])
ax.set_xlabel('Age')
ax.set_ylabel('CreditScore')
plt.show()


# In[11]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c

