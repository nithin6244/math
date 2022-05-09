#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sympy import *
import numpy as np
from sympy import integrate

x,y = symbols("x,y")
def p(x,y):
    return 3*(x**2)-8*(y**2)
dp = diff(p(x,y),y)

def q(x,y):
    return 4*y-6*x*y
dq = diff(q(x,y),x)

s = dq-dp
z1 = integrate(s,(y,0,2),(x,0,1))
print(z1)

F = np.array([p(x,y),q(x,y)])

x1 = 1
dx = diff(x1,x)
dy = diff(y,y)
dt1 = np.array([dx,dy])
H1 = np.dot(F,dt1)
H2 = H1.subs(x,1)
I1 = integrate(H2,(y,0,2))
print(I1)


x2 = 0
dx = diff(x2,x)
dy = diff(y,y)
dt2 = np.array([dx,dy])
H13 = np.dot(F,dt2)
H4 = H13.subs(x,0)
I2 = integrate(H4,(y,2,0))
print(I2)

y1 = 0
dx = diff(x,x)
dy = diff(y1,x)
dt3 = np.array([dx,dy])
H13 = np.dot(F,dt3)
H23 = H13.subs(y,0)
I3 = integrate(H23,(x,0,1))
print(I3)

y2 = 2
dx = diff(x,x)
dy = diff(y2,x)
dt4 = np.array([dx,dy])
H14 = np.dot(F,dt4)
H24 = H14.subs(y,2)
I4 = integrate(H24,(x,1,0))
print(I4)

z = I1+I2+I3+I4
print(z)

if(z==z1):
    print("Green's theorm is verified")
else :
    print("Green's theorm is not verified")


# In[ ]:




