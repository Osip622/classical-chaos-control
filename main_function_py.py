#!/usr/bin/env python
# coding: utf-8

# In[6]:


import seaborn as sns
import numpy as np
from scipy.integrate import odeint
'''import scipy.integrate as integrate'''
import matplotlib.pyplot as plt
import matplotlib
import math
import statistics
import sys
import operator
import collections
import time
import pandas as pd
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import fmin_cobyla
#from IPython.display import clear_output


# In[9]:


get_ipython().run_line_magic('run', 'harvester_function.ipynb     #this is were my function is stored')
get_ipython().run_line_magic('run', 'optimization_function.ipynb')


# In[16]:


g=2.565
gam=0.02
om=0.16
xi=0.05
R=1 #param
C=0.25
X = np.array([ -1.2167034 ,  0.94510265, -0.02208411,  0.60319202,  0.09466782])


# In[17]:


global g, gam, om, xi, C, X
save_data = []
save_input = []
save_array = []
save_time = [0]
optimization_function(1)


# In[ ]:





# In[ ]:




