
# coding: utf-8

# ## 파이썬 함수 구조

# def 함수명(입력 인수):
#     수행문장~
#     return 결과값

# In[1]:


def sum(a,b):
    return a+b
a=3
b=4
c= sum(a,b)
print(c)


# ## 입력값과 결과값에 따른 함수의 형태

# ### 일반적인 함수
# #### def 함수명(입력인수):
# - 수행할문장
# - return 결과값
# ##### 결과값을 받을 변수 = 함수명(입력인수1, 2..)

# In[2]:


def sum(a,b):
    result = a+b
    return result

a=sum(3,4)
print(a)


# ### 입력값이 없는 함수
# #### def 함수명():
# - return 결과값
# ##### 결과값을 받을 변수 = 함수명()

# In[3]:


def say():
    return 'Hi~'
a=say()
print(a)


# ### 결과값이 없는 함수
# #### def 함수명(입력인수):
# - print()
# ##### 함수명(입력인수1,2...)

# In[6]:


def sum(a,b):
    print('%d,%d의 합은 %d입니다' %(a,b,(a+b)))

a=sum(3,4)
print(a)


# ### 입력값도 출력값도 없는 함수
# #### def 함수명():
# - print()
# ##### 함수명()

# In[8]:


def say():
    print('hi')
    
say()


# ## 입력값이 몇 개가 될지 모를때 ??

# #### def 함수명(*입력변수):
# - 수행할문장
# - *은 입력변수를 튜플로 변환시켜줌!!

# In[10]:


def sum_many(*args):
    sum=0
    for i in args:
        sum = sum+i
    return sum

print(sum_many(1,2,3))
print(sum_many(1,2,3,4,5))


# In[23]:


def cal(choice,*args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result=1
        for i in args:
            result = result * i
    return result

a=cal("sum", 1,2,3)  
print(a)
print(cal("mul", 1,2,3))


# ## 함수의 결과값은 언제나 하나이다!

# return a,b를 쓸 경우 튜플로 결과를 보여줌

# In[26]:


def sum_and_mul(a,b):
    return a+b,a*b

sum_and_mul(3,4)
sum,mul = sum_and_mul(3,4)
print(sum)
print(mul)


# return을 두번 쓸 경우 처음 return을 만나고 함수가 종료되므로 두번재는 실행안됨

# In[27]:


def sum_and_mul(a,b):
    return a+b
    return a*b

sum_and_mul(3,4)


# 리턴을 만나면 함수를 빠져나가기 때문에 이를 이용하는 경우가 많음

# In[28]:


def say_nick(nick):
    if nick == '바보':
        return
    print('내 별명은 %s입니다.' %nick)
    
say_nick("야호")
say_nick("바보")
say_nick("천재")


# ## 입력 인수에 초깃값 미리 설정

# In[32]:


def say_myself(name,old,man=True):
    print('나의 이름은 %s입니다\n'%name)
    print('나이는 %d입니다\n' %old)
    if man:
        print('남자입니다\n')
    else:
        print('여자입니다\n')
        
say_myself('윤원식',31,True)
say_myself('윤여성',31,False)


# 초기화시키고 싶은 입력 변수들을 항상 뒤쪽에 위치시켜야 한다!

# In[33]:


def say_myself(name,man=True,old):
    print('나의 이름은 %s입니다\n'%name) 
    if man:
        print('남자입니다\n')
    else:
        print('여자입니다\n')
        print('나이는 %d입니다\n' %old)
        
        
say_myself('윤원식',True,31)
say_myself('윤여성',False,31)


# ## 함수 안에서 선언된 변수의 효력 범위

# In[39]:


a =1
def vartest(a):
    a=a+1

vartest(a)
print(a)


# In[46]:


def vartest(k):
    k=k+1

vartest(3)
print(k)


# 함수 안에서 함수 밖의 변수를 변경하는 방법

# retrun 이용하기!

# In[47]:


l=1
def vartest(l):
    l=l+1
    return l

l=vartest(l)
print(l)


# global 명령어 (가급적 사용 x)

# In[49]:


j=1
def vartest():
    global j
    j=j+2

vartest()
print(j)

