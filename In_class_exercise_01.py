#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/unt-iialab/INFO5731_Spring2020/blob/master/In_class_exercise/In_class_exercise_01.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # **The first In-class-exercise (9/2/2020, 20 points in total)**

# (1) Write a Python program to calculate the length of a string. (2 points)

# In[14]:


# write your answer here
is_name = "Pandey"
print("The length of the string is :",len(is_name))


# (2) Write a Python program to count the number of characters in a string. (2 points)
# 
# Sample String : 'google.com‘, 
# 
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# In[80]:


#write your answer here 
def is_count(character):
    dict={}
    for x in character:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
                 dict[x] = 1          
    return dict
print(is_count('google.com'))
        
        
    


# (3) Write a Python program to sum all the items in a list. (2 points)

# In[72]:


# write your answer here

def sum_list(items): #user defined function 
    sum_numbers=0   # adding with this number 
    for x in items:
        sum_numbers +=x
    return sum_numbers 
print(sum_list([1,2,3,4,5]))
    


# (4) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '\$', except the first char itself. (2 points)
# 
# Sample String : 'restart‘, 
# 
# Expected Result : 'resta\$t'

# In[94]:


# write your answer here
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))


# (5) Write a program with python which could accept two parameter a and b to calculate and output the result of S, where 
# 
# $\ S=3.14*(1+a/b)^3$ (3 points)
# 
# 

# In[101]:


# write your answer here

def calculate(a,b):
    s=3.14*(1+𝑎/𝑏)**3
    return s
print(calculate(5,4))


# (6) Write a Python program to concatenate following dictionaries to create a new one. (3 points)
# 
# Sample Dictionary : dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50,6:60}, 
# 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# 

# In[90]:


# write your answer here
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# (7) Write a Python program to check whether an element exists within a tuple. (3 points)

# In[84]:


# write your answer here
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)


# (8) Write a Python program to find maximum and the minimum value in a set. (3 points)

# In[82]:


# write your answer here
#Create a set
seta = set([4, 5, 6, 15, 2, 15])
#Find maximum value
print(max(seta))
#Find minimum value
print(min(seta))


# (9) Write a Python program to randomly divide the students in this class into five groups for term projects, each group should have at least 3 students but no more than 5 students (including 5). Here is the students list: (3 points for extra)
# 
# studnet_list = ['vmb0067','pc0353','snd0097','yye0005','sg0940','bk0301','rak0120','rrk0058','spk0057','vl0135','nm0547','pn0159',
#                 'msp0174','dd0420','ds0761','rs0850','ss1995','at0739','at0768','mv0299','tv0119','dy0091']

# In[182]:


# write your answer here
import random 
student_list =['vmb0067','pc0353','snd0097','yye0005','sg0940','bk0301','rak0120','rrk0058','spk0057','vl0135','nm0547','pn0159', 'msp0174','dd0420','ds0761','rs0850','ss1995','at0739','at0768','mv0299','tv0119','dy0091']
#type(student_list)
length=len(student_list)
#print (length)
groups = 5
while students > 0 and groups > 0:
    grp=random.sample(student_list, int(students/groups))
    for x in grp:
        student_list.remove(x)
    students -= int(students/groups)
    groups -=1
print(grp)
        
        







