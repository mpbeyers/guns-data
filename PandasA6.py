#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


q1 = pd.read_csv('dots.csv')
q1


# In[3]:


Q1 = q1.firing_rate.mean()
Q1


# In[4]:


Q2 = q1.time.max()
Q2


# In[5]:


Q3 = q1.groupby('choice').mean()
Q3


# In[6]:


Q4 = q1.groupby('align')['firing_rate'].min()
Q4


# In[7]:


Q5 = q1.groupby(['align', 'choice'])['firing_rate'].aggregate('mean').unstack()
Q5


# In[8]:


Q6 = q1.pivot_table('firing_rate', 'align', 'choice')
Q6


# In[9]:


tips = pd.read_csv('tips.csv')
tips


# In[10]:


Q7 = tips.pivot_table('total_bill', ['sex', 'smoker'], 'time')
Q7


# In[11]:


tip = pd.cut(tips['tip'], [0, 5, 10])


# In[12]:


Q8 = tips.pivot_table('total_bill', ['sex', tip], 'smoker')
Q8


# In[13]:


Q9 = tips.pivot_table(index='sex', columns='smoker',
                   aggfunc={'size':sum, 'tip':max, 'total_bill':'mean'})
Q9


#adding a note: commit to github
