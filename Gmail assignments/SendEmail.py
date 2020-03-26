#!/usr/bin/env python
# coding: utf-8

# In[6]:


import smtplib
from email.message import EmailMessage

user='userid'
pwd='pwd'
smtp_url='smtp.gmail.com'
from_address=user
to_address= ["intellipaat.sarika@gmail.com","sarikaspawar@gmail.com","sarikaspawar09@gmail.com","joemtech75@gmail.com"]
mail=smtplib.SMTP_SSL(smtp_url)
mail.login(user,pwd)

msg = EmailMessage()
msg['Subject'] = 'Sending email using python to Joe'
for to in to_address:
    msg.set_content("Hi "+str(re.split("@",to)[0])+",\nHope you are doing well\nPlease review my gmail assignment\nhttps://github.com/intellipaatsarika/python-code/")
    print(re.split("@",to)[0])
    mail.sendmail(from_address,to,msg.as_string())


# In[ ]:




