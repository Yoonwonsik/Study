
# coding: utf-8

# 문자열

# In[6]:


pin ="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)


# In[7]:


print(num)


# In[8]:


print(pin[7:8])


# 리스트

# In[10]:


a=[1,3,5,4,2]
a.sort()
a.reverse()
a


# In[18]:


a=['Life','is','to','short']
result=" ".join(a)
print(result)


# 튜플

# In[23]:


a=(1,2,3)
a=a+(4,)
print(a)


# 딕셔너리

# In[24]:


a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)


# 집합

# In[28]:


a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set([1,1,1,2,2,3,3,3,4,4,5])
b=list(aSet)
print(b)


# 변수

# In[30]:


a=b=[1,2,3]
a[1]=4
print(b)


# a,b 둘다 [1,2,3]이라는 리스트를 가리키고 있기 때문
