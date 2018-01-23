
# coding: utf-8

# if문

# In[1]:


a = "Life is too short, you need python"
if "wife" in a : print("wife")
elif "python" in a and "you " not in a:print("python")
elif "shirt" not in a:print("shirt")
elif "need" in a:print(need)
else:print("none")


# while문

# 별이 증가하는거 만들기~

# In[10]:


i=1
while i<=5:
    print("%s" %"*"*i) #print("*"*i) 로 해답은. ..
    i= i+1


# for문

# [70,60,55,75,95,90,80,80,85,100]  학급 평균 점수 구하기

# In[18]:


scores= [70,60,55,75,95,90,80,80,85,100]
total =0
for number in range(len(scores)): #해답은 number in scores
    total = total+scores[number]     #total= total+number 로 되어있음
print("총점수는 : %d" %total)
average = total/len(scores)
print("평균은 : %.1f" %average)

