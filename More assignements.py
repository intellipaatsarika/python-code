#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Compare two list's elements
#lists, for and if else
L1=[1,2,3,8,5,6,1]
L2=[6,5,4,8,2,1,5]
for x in range(len(L1)):
    if(L1[x]<L2[x]):
        print("L1 list's element "+str(x)+" is less than L2 element")
    elif(L1[x]>L2[x]):
        print("L1 list's element "+str(x)+" is greater than L2 element")
    else:
        print("L1 list's element "+str(x)+" is equal to L2 element")


# In[14]:


T1=(10,20,30,40,50)
for x in T1:
    print(x+5)


# In[16]:


def add_10(n):
    return n+10

print(add_10(6))


# In[22]:


#odd even numbers
def check_odd_even(n):
    if(n==0):
        print(n,":Whole number") 
    elif(n%2==0):
        print(n,":Even number")
    else:
        print(n,":odd number")

for x in range(10):
    check_odd_even(x)


# In[44]:


#leap year
def is_leapYear(Y):
    if(Y%400==0 or Y%100!=0 and Y%4==0):
        print(Y,":LEAP Year")
    else:
        print(Y,":No leap year")
    
for y in range(1990,1998):
    is_leapYear(y)


# In[50]:


#take list and return even number of list
def even_list(L):
    list=[]
    for x in L:
        if (x%2==0):
            print(x,"even number")
            list.append(x)
        else:
            print(x,"odd number")
    return list   

            
l=[1,2,3,4,5,6,8,10,91]            
print(even_list(l))


# In[61]:


#List with square of numbers from 1 to 10
def squares(n):
    listSq=[]
    for x in range (n):
        listSq.append(x*x)
    return listSq

print(squares(10))

#use list comprehension, it returns list
#new_list = [expression for member in iterable]
squares=[i*i for i in range(10)]
print(squares)

'''
List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions'''


# In[65]:


list=[5,6,7,8,9]
sum=0
for x in list:
    print(x)
    sum=sum+x
print(sum)
    


# In[80]:


t1=(10,20,30)
t2=(40,50,60)
t_combine=t1+t2
print(t_combine)
print(t_combine*3)
print(t_combine[2])
print(t_combine[0:3])
print(t_combine[-3:])


# In[85]:


my_list=[(1,2,3),("a","b","c"),(True,False)]
my_list.append((1,"a",True))
print(my_list)
new_list=["sparta",123]
print(my_list+new_list)


# In[91]:


#to assign multiple values to one key. can use tuple, list or dictionary
my_dict={"fruits":["apple","banana","mango","guava"],
        "cost":[85,67,65,86]}
print(my_dict.keys())
print(my_dict.values())


# In[95]:


mySet={6,2,"a","sarika",True,False,"a"}
print(mySet)
for x in mySet:
    print(x)


# In[132]:


L1=[1,5,8,9,6]
L2=[6,7,3,1,9]
for i in range (len(L1)):
    for j in range (len(L2)):
        if(L1[i]==L2[j]):
            print(L1[i])
            break

#Now use list comprehension
def matchElement(l1,l2):
    n=len(L1)
    m=len(L2)
    print(m)
    print(n)
    matchL=[L1[i] for i in range(n) for j in range(m) if(L1[i]==L2[j])]  #list comprehension
    print(matchL)
    

L1=[1,5,8,9,6]
L2=[6,7,3,1,9]
matchElement(L1,L2)
        


# In[127]:


L1=[1,5,8,9,6]
L2=[6,7,3,1,9]
for i in range (len(L1)):
    for j in range (len(L2)):
        if(L1[i]==L2[j]):
            print(L1[i])
            break

