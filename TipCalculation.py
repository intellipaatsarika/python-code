#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tip calcualtion
def tipCalc(tBill):
    tip=tBill*10/100
    print("Tip for total bill of Rs."+str(tBill)+ " is " +str(tip))
    return tip


tipCalc(100)
tipCalc(200)
tipCalc(300)

