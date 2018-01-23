
# coding: utf-8

# ## 집합 자료형 만들기

# In[1]:


s1=set([1,2,3])
s1


# In[2]:


s2=set("배고파")
s2


# In[3]:


s3=set("hello")
s3


# ## 집합 자료형 특징

# 집합자료형 => 중복허용x, 순서x
# 순서가 없으므로 인덱싱 안됨

# In[8]:


l1=list(s1)
l1
l1[0]


# In[9]:


t1=tuple(s1)
t1


# 즉 인덱싱 하려면 리스트 및 튜플로 변환해야함

# ## 집합 자료형 활용방법

# 교집합, 합집합, 차집합 구하기~

# 교집합 => 변수1&변수2 로 쓰면 됨 or 변수1.intersection(변수2)

# In[12]:


s1=set([1,2,3])
s2=set([3,4,5])
s1&s2


# In[14]:


s1.intersection(s2)


# 합집합 => 변수1|변수2 or 변수1.union(변수2)

# In[15]:


s1|s2


# In[16]:


s1.union(s2)


# 차집합 => 변수1-변수2 or 변수1.difference(변수2)

# In[17]:


s1-s2


# In[18]:


s1.difference(s2)


# ## 집합 자료형 관련 함수들

# add 값 1개 추가하기 => 변수.add(x)

# In[21]:


s1.add(4)
s1


# update 값 여러개 추가하기 =>변수.update([])

# In[24]:


s1.update(5)
s1


# In[25]:


s1.update([6,7])
s1


# remove 특정값 제거하기 => 변수.remove() 

# In[26]:


s1.remove(7)
s1


# In[27]:


s1.remove([5,6])
s1


# In[29]:


s12=set([2])
s12


# In[32]:


s12.add(1)
s12


# In[33]:


s12.update([3])
s12

