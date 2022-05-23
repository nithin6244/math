#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sympy as sp
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform

U = laplace_transform(sp.expand((1+t)**3), t, s)
print(U)


# In[19]:


import sympy as sp
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
n = (sp.exp(-3*t))*(sp.sin(4*t))
U = laplace_transform(n, t, s)
print(U)


# In[20]:


import sympy as sp
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform

U = laplace_transform(2*sp.sin(t)*sp.sin(3*t), t, s)
print(U)


# In[23]:


import sympy as sp
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform

U = laplace_transform(sp.cos(3*t)**2, t, s)
print(U)


# In[ ]:




