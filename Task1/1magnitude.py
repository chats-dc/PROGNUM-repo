#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = input("Enter apparent magnitude: ")
m_int = int(m)
M = input("Enter absolute magnitude: ")
M_int = int(M)

d = 10.0 * pow( 10.0, (m_int-M_int)/5.0 ) * 3.26164
print(f"The distance is: {d:5.3f} parsecs")


# In[ ]:




