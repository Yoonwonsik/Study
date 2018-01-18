
# coding: utf-8

# # 튜플~?

# 튜플은 리스트와 몇가지를 제외하고는 거의 비슷
# 
# 차이점 : 리스트는 []를 사용, 튜플은 ()를 사용
#         리스트는 값의 생성, 수정, 삭제 가능 튜플은 그 값을 바꿀 수 없음

# In[3]:


#기본 생긴게 이리 생김
t1=()
t2=(1,)  #1개의 요소만 가질때는 콤마(,)를 반드시 붙여야됨
t3=(1,2,3)
t4=1,2,3 #괄호생략가능
t5=('a','b',('ab','cd'))


# In[5]:


t2=1,


# In[6]:


t2


# In[7]:


del t2[0]


# ## 튜플 인덱싱 및 슬라이싱, 더하기 곱하기~

# 인덱싱

# In[8]:


t1=(1,2,'a','b')
t1[0]


# 슬라이싱

# In[9]:


t1[1:]


# 더하기

# In[11]:


t2=(3,4)
t1+t2


# 곱하기

# In[13]:


t1*3

