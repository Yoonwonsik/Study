
# coding: utf-8

# ## 변수를 만드는 여러가지 방법

# In[6]:


a,b = ("Python",'life')
a


# In[7]:


b


# In[8]:


(c,d)='pyhon','Life'
c


# In[9]:


d


# In[10]:


[a,b]=['pYthon','lIfe']
a


# In[11]:


b


# In[12]:


a=1
b=2
a,b=b,a
a


# In[13]:


b


# ## 메모리에 생성된 변수 없애기

# 변수없애기 => del(변수명)

# In[14]:


a=3
a


# In[15]:


del(a)
a


# ## 리스트를 변수에 넣고 복사

# In[16]:


a=[1,2,3]
b=a
a[1]=4
a


# In[17]:


b


# 리스트 살리기 ?

# In[20]:


a=[1,2,3]
b=a[:]
a[1]=4
a


# In[21]:


b


# 리스트 살리기2! a[:] = copy[a] (대신 copy 써주려면 from copy import copy 해줘야함
