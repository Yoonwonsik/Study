
# coding: utf-8

# ## 사용자 입력

# input의 사용! , 입력되;ㄴ느 모든 것을 문자열로 취급!

# In[2]:


a=input()


# In[3]:


a


# 프롬프트 띄워서 사용자 입력 받기

# input()의 괄호 안에 질문을 입력하여 띄워주면 됨!

# In[4]:


input("입력해주세요!")


# In[5]:


number = input("숫자를 입력해주세요 : ")


# In[6]:


print(number)


# ## print 자세히 알기!

# 큰따옴표(")로 둘러싸인 문자열은 +연산과 동일하다!

# In[7]:


print("Life" "is" "short")
print("Life"+"is"+"short")


# 문자열 띄어쓰기는 콤마!

# In[8]:


print("Life","is","short")


# 한줄에 결과값 입력하기! end="를 이용!!

# In[11]:


for i in range(10):
    print(i,end=' ')

