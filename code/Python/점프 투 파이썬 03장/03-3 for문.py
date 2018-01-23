
# coding: utf-8

# ## for문 기본구조

# In[1]:


test_list = ['one','two','three']
for i in test_list:
    print(i)


# In[2]:


test_list = [(1,2),(3,4),(5,6)]
for (first,second) in test_list:
    print(first+second)


# In[8]:


score = [60,65,67,45,80]
number =0
for mark in score:
    number = number+1
    if mark>=60:
        print("%d번째 학생은 합격!" %number)
    else:
        print("%d번째 학생은 불합격!" %number)


# ## for문과 continue

# In[10]:


score = [60,65,67,45,80]
number =0
for mark in score:
    number = number+1
    if mark<60:continue
    print("%d번째 학생은 합격!" %number)


# ## range 함수!!

# In[11]:


a=range(10)
a


# range(0,10) < 0~9까지!  끝 숫자는 포함 안됨

# In[12]:


sum=0
for i in range(1,11):
    sum=sum+i
print(sum)


# In[21]:


score = [60,65,67,45,80]
for number in range(len(score)):
    if score[number]<60:continue
    print("%d번째 학생은 합격!" % (number+1))


# In[29]:


for i in range(2,3):
    for j in range(1,10):
        print("%d단 : %d" %(i,i*j))


# ## 리스트 안에 for문 포함 

# In[31]:


a=[1,2,3,4]
result=[]
for num in a:
    result.append(num)
    
print(result)


# In[32]:


a=[1,2,3,4]
result=[num for num in a]
print(result)


# In[33]:


a=[1,2,3,4]
result=[num for num in a if num % 2==0]
print(result)


# 리스트 내포 문법 => [표현식 for 항목 in 가능객체 if 조건]

# In[35]:


result=[i*j for i in range(2,10)
               for j in range(1,10)]
print(result)

