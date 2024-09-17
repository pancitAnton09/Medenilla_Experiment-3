#!/usr/bin/env python
# coding: utf-8

# # Experiment 3
# ## Python Data Analysis (Pandas)

# In[65]:

# Access pandas' function
import pandas as pd

# ### Problem 2

# In[183]:


# Using DataFrame carlist, extract the .csv file 
carlist = pd.read_csv('cars.csv')


# In[187]:


# Display the first five rows with odd-numbered columns of cars.
## Slice the DataFrame, starting from row 1 with an increment of 2
### Then, use .head() to display first five rows
carlist[1::2].head()


# In[189]:


# Use .loc to display the row that contains the ‘Model’ of ‘Mazda RX4’
## In this case row [0], and the column ['Model'] will be extracted
carlist.loc[[0],['Model']]


# In[191]:


# Use .loc to determine how many cylinders does the 'Camaro Z28' have
## In this case row [23], and the columns ['Model', 'cyl'] will be extracted
carlist.loc[[23],['Model','cyl']]


# In[193]:


# Use .loc to determine how many cylinders and what gear type do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
## In this case, rows [1,28,18] and columns ['Model', 'cyl', 'gear'] will be extracted
carlist.loc[[1,28,18],['Model', 'cyl', 'gear']]

