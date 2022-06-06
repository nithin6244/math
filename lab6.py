#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sympy.integrals.transforms import inverse_laplace_transform

from sympy.abc import s, t
gfg = inverse_laplace_transform(1/(s+3)**2, s, t)
 
print(gfg)


# In[4]:


from sympy.integrals.transforms import inverse_laplace_transform

from sympy.abc import s, t
gfg = inverse_laplace_transform(1/(s+3)**3, s, t)
 
print(gfg)


# In[5]:


from sympy.integrals.transforms import inverse_laplace_transform

from sympy.abc import s, t
gfg = inverse_laplace_transform(2/(s-3)**5, s, t)
 
print(gfg)


# In[6]:


from sympy.integrals.transforms import inverse_laplace_transform

from sympy.abc import s, t
gfg = inverse_laplace_transform((2*s-11)/(s**2+4*s+8), s, t)
 
print(gfg)


# In[8]:


from sympy.integrals.transforms import inverse_laplace_transform

from sympy.abc import s, t
gfg = inverse_laplace_transform(((3*s)**2+10*s-6)/(s**4), s, t)
 
print(gfg)


# In[ ]:




