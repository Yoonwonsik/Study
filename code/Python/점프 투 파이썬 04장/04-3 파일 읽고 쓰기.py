
# coding: utf-8

# ## 파일 생성하기

# ### 파일객체 = open(파일이름,파일열기모드)
# - 파일열기모드
# - r : 읽기모드 - 파일을 읽기만 할 때 사용
# - w : 쓰기모드 - 파일에 내용을 쓸 때 사용
# - a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 할 때 사용

# In[1]:


f=open("새파일.txt",'w')
f.close()


# 디렉터리에 생성하기.. 

# In[4]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'w')
f.close()


# f.close는 열려있는 파일 객체를 닫아주는 역활 안써줘도 되긴함(프로그램을 종료할 때 파이썬이 열려 있는 파일의 개체를 자동으로 닫아주기 때문) 그래도 열려있는거 다시 사용하려 하면 오류 나기 때문에 닫고 쓰고 하는 걸 익숙하게 하자..

# ## 파일을 쓰기 모드로 열어 출력값 적기

# In[5]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


# f.write(data) << data를 파일 객체 f에 써라!!
# print(data)와의 차이는 print는 화면에 f.write는 파일에 !!

# ## 프로그램 외부에 저장된 파일을 읽는 여러가지 방법

# readline()함수 이용하기

# In[6]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'r') #r은 읽기모드
line = f.readline()
print(line)
f.close()


# In[7]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'r') #r은 읽기모드
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()


# In[8]:


while True:
    data = input()
    if not data:break
    print(data)


# 위와 아래의 차이는 입력받는 방식만 다른(파일에서 가져오냐 입력을 받느냐~)

# readlines()사용! 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스토로 리턴!

# In[16]:


f=open("C:/Users/YWS/Desktop/새파일2.txt",'r') #r은 읽기모드
lines = f.readlines()
for line in lines:
    print(line)

print(lines)
f.close()


# read()함수 파일의 내용 전체를 문자열로 리턴!

# In[11]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'r') #r은 읽기모드
data=f.read()
print(data)
f.close()


# In[15]:


f=open("C:/Users/YWS/Desktop/새파일2.txt",'r') #r은 읽기모드
data=f.read()
print(data)
f.close()


# ## 파일에 새로운 내용 추가하기

# In[17]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'a') #a은 추가모드!
for i in range(11,21):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


# In[18]:


f=open("C:/Users/YWS/Desktop/새파일.txt",'r') #r은 읽기모드
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()


# ## with문과 함께 사용하기

# 위에서 언급한 close를 자동으로 처리하기 위한!!

# In[19]:


f=open("C:/Users/YWS/Desktop/새파일3.txt",'w')
f.write("추어... 집에 언제 가냥...")
f.close()


# In[21]:


with open("C:/Users/YWS/Desktop/새파일4.txt",'w') as f:
   f.write("추어... 집에 언제 가냥...")


# 위 아래가 같은 문장인데 f.close를 쓰지 않고 파일객체 선언자리에 with를 넣고 오픈 뒤에 as (파일객체) : 를 써주면 됨~~ 
