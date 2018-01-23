
# coding: utf-8

# ## while 기본구조

# In[ ]:


treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit==10:
        print("나무 넘어갑니다~")


# ## while문 직접 만들기

# In[ ]:


prompt="""
1.ADD
2.DEL
3.List
4.Quit

Enter number:"""

number=0
while number!=4:
    print(prompt)
    number = int(input())


# ## While문 강제로 빠져나가기

# In[ ]:


coffee = 100
money = 300
machinemoney=0
while money:
    if coffee-35>0:
        print("돈을 주셨으니 커피를 드립니다")
        coffee = coffee -35
        print("남은 커피 양은 %d개 입니다" %coffee)
    else :
        print("커피가 다 떨어졌습니다 판매중지!")
        break
    


# In[4]:


coffee =10
while True:
    money = int(input("돈을 넣어주세요:"))
    if money==300:
        print("돈을 주셨으니 커피를 드립니다 거스름돈은 없습니다.")
        coffee=coffee-1
    elif money>300:
        print("돈을 주셨으니 커피를 드립니다 거스름돈은 %d원 입니다." % (money-300))
        coffee=coffee-1
    else:
        print("돈이 모자릅니다. 모자른돈은 %d원 입니다" % (300-money))
    if not coffee:
        print("SOLD OUT!!")
        break


# ## 조건에 맞지 않는 경우 맨 처음으로!!

# In[10]:


a=0
while a<10:
    a=a+1
    if a%2==0:continue
    print(a)


# contunue : 참일경우 처음으로 돌아가게 함.. 근데 구지 안써도 되니 쓰지 말자... !=0으로 하면 홀수 출력됨

# ## 무한루프

# In[11]:


while True:
    print("ctrl+c를 눌러야 while 문을 빠져나갈수 있습니다!")

