#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Cumulative sum
def cumSumList(l):
    csumList=[]
    n=len(l)
    for i in range(n):
        csumList.append(sum(l[0:i+1]))
    print(csumList,"--Using list")

def cumSumComp(l1):
    csumList=[sum(l1[0:i+1]) for i in range (len(l1))]
    print(csumList,"--Using list comprehension")
    

L=[1,6,7,8,9]
cumSumList(L)
cumSumComp(L)

