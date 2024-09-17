#!/usr/bin/env python
# coding: utf-8

# # Experiment 3
# ## Python Data Analysis (Pandas)

# In[65]:


# Access pandas' function
import pandas as pd


# ### Problem 1

# In[177]:


# Load the car.csv file into DataFrame carlist
carlist = pd.read_csv('cars.csv')


# In[179]:


# Display the first five rows of the resulting carlist ( using .head())
carlist.head()


# In[181]:


# Display the last five rows of the resulting carlist (using .tail())
carlist.tail()