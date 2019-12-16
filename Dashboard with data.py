#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In[2]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# In[3]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# In[4]:


dfgdp = pd.read_csv(links["GDP"])
dfgdp.head()


# In[5]:


dfunemp = pd.read_csv(links["unemployment"])
dfunemp.head()


# In[8]:


unemp85 = dfunemp[dfunemp['unemployment'] > 8.5]
unemp85


# In[10]:


x = dfgdp['date']
gdp_change = dfgdp['change-current']
unemployment = dfunemp['unemployment']
title = 'Us economy data'
file_name = 'index.html'


# In[11]:


make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)


# In[ ]:




