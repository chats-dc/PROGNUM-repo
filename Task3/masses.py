#!/usr/bin/env python
# coding: utf-8

# ### 3.1

# In[34]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
masses2=masses.copy()

i=0
for i in range(len(masses)): 
    if masses[i]<7.349e+22:
        
        del masses[i]
        i+=1
    else: 
        ()
        
print(masses)
print(masses2)


# In[42]:


indices = slice(-6,None,1)
sliced=masses2[indices]
print(sliced)


# In[44]:


mean = sum(sliced)/len(sliced)
print(mean)


# 
