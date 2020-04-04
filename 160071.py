#!/usr/bin/env python
# coding: utf-8

# In[184]:


import matplotlib as plt
import numpy as np
import pandas as pd
import sqlite3


# In[185]:


data_multi_age=pd.read_csv("multilingual-age.csv")
data_multi_ed=pd.read_csv("multilingual-education.csv")
data_age_ed=pd.read_csv("age-education.csv")


# In[186]:


data_age_ed.columns=['Table_name','State_code','Dist_code','Area_name','Total_Rural_Urban','Age_group','A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3','E1','E2','E3','F1','F2','F3','G1','G2','G3','H1','H2','H3','I1','I2','I3','J1','J2','J3','K1','K2','K3','L1','L2','L3','M1','M2','M3']
data_multi_age.columns=['State_code', 'District_code', 'Area_name', 'Total_pop', 'Age_group', 'Total2', 'Male2', 'Female2', 'Total3', 'Male3', 'Female3']
data_multi_ed.columns=['State_code', 'District_code', 'Area_name', 'Total_Rural_Urban', 'Education', 'T2', 'M2', 'F2', 'T3', 'M3', 'F3']
data_age_ed


# In[187]:


data_age_ed.drop([0,1,2,3,4,5],inplace=True)
data_multi_age.drop([0,1,2,3],inplace=True)
data_multi_ed.drop([0,1,2,3],inplace=True)
data_age_ed


# In[ ]:





# In[188]:


for columns in list(data_age_ed.columns.values):
    data_age_ed[columns] = pd.to_numeric(data_age_ed[columns],errors='ignore')

for columns in list(data_multi_age.columns.values):
    data_multi_age[columns] = pd.to_numeric(data_multi_age[columns],errors='ignore')
for columns in list(data_multi_ed.columns.values):
    data_multi_ed[columns] = pd.to_numeric(data_multi_ed[columns],errors='ignore')
# print data_age_ed.dtypes


# In[189]:


result = data_age_ed.dtypes
result
# data_age_ed


# In[190]:


conn = sqlite3.connect('population.db')
c = conn.cursor()
data_age_ed.to_sql('age_ed',conn,if_exists='append', index=False)
data_multi_age.to_sql('multi_age',conn,if_exists='append', index=False)
data_multi_ed.to_sql('multi_ed',conn,if_exists='append', index=False)


# In[191]:


data_age_ed


# In[192]:


data_multi_age


# In[193]:


data_multi_ed


# In[ ]:




