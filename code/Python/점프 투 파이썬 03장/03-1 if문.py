
# coding: utf-8

# ## 예시

# In[9]:


money = 1
if money:
    print("택시타")
else:
    print("걸어가")


# ## 조건문이란..?

# 조건문 : 참 거짓을 판단하는 문장
# 
# 숫자  => 참 : 0아닌 숫자 / 거짓 : 0
# 
# 문자열,리스트, 튜플, 딕셔너리=> 참 : 있는거 / 거짓 : 없는거

# 비교 연산자
# > , < , == , != , >=, <= 등이 있음~

# 3천원 이상 돈을 가지고 있으면 택시, 안그러면 걸어~ 

# In[10]:


money = 2000 #2천원 가지고 있음
if money >=3000:
    print("택시!")
else:
    print("걸어")


# or , and, not
# 
# or : 둘중 하나만 참이면 참
# 
# and : 둘다 참이여야 참
# 
# not : 거짓이면 참! (반대)

# 3천원 이상 돈 있거나 카드 있으면 택시타~ 아님 걸어

# In[11]:


money = 2000 # 돈
card =1 #카드유무 (1은 있는거, 0은 없는거)
if money>=0 or card :
    print("택시")
else :
    print("걸어!")


# x in s // x not in s
# 
# x가 s(리스트, 튜플, 문자열 등~)안에 있는가??

# In[12]:


1 in [1,2,3]


# In[13]:


1 not in (1,2,3)


# In[15]:


'a' in 'abc' 


# 주머니안에 돈이나 카드 있으면 택시타고가

# In[16]:


pocket = ['phone','key','card']
if 'money'or'card'in pocket:
    print("택시 타")
else :
    print("걸어")


# ## 다양한 조건 판단 elif

# 다른 코딩에서 쓰던 else if가 여기서는 elif로 쓰임

# 주머니에 돈있으면 택시, 주머니에 돈은 없지만 카드 있으면 택시! 아니면 걸어

# In[18]:


pocket = ['phone','key']
card = 0
if 'money' in pocket:
    print("택시타")
else:
    if card:
        print('택시')
    else :
        print('걸어')


# In[19]:


pocket = ['phone','key']
card = 0
if 'money' in pocket:
    print("택시타")
elif card:
    print('택시')
else :
    print('걸어')

