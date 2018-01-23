
# coding: utf-8

# ## 딕셔너리??

# 기본 생긴건 {Key1:Value1, Key2:Value2 ..}
# ex ) dic = {'name':'원식','state':배고픔}

# 딕셔너리 쌍 추가, 삭제

# In[1]:


a={1:'a'}
a[2]='b'
a


# In[2]:


address = {"시":'서울시','구':'성북구'}
address['동']='돈암동'
address


# In[3]:


address['나라']='대한민국'
address


# In[4]:


address.sort()


# In[5]:


del address['나라']
address


# ## 딕셔너리 사용방법

# key값을 통한 value얻기

# In[7]:


address['구']


# In[ ]:


a={1:"a",1:"b"}
a[1]


# ## 딕셔너리 관련 함수

# key 리스트 만들기 리스트명.keys() dict_keys로 만들어진다. list화 시키고 싶으면 list(.keys())

# In[8]:


address.keys()


# In[9]:


list(address.keys())


# In[10]:


for k in address.keys():
    print(k)


# value 리스트 만들기 리스트명.values()

# In[11]:


for k in address.values():
    print(k)


# key, value 쌍으로 얻는것 리스트명.items()

# In[12]:


address.items()


# key value 쌍 모두 지우기 리스트.clear()

# In[16]:


address.clear()
address


# key로 value 얻기 리스트.get(key)

# In[21]:


address = {"시":'서울시','구':'성북구'}
address.get('시')


# In[22]:


address['시']


# In[25]:


address.get('동')


# In[24]:


address['동']


# In[26]:


address.get('동','돈암동')


# In[27]:


address.get('시','돈암동')


# In[28]:


address.get('동')


# 해당 key가 있는지 조사 key in 리스트명

# In[29]:


'시' in address


# In[30]:


'동' in address

