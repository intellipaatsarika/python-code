#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Extract emails from Gmail from Session 5  - use IMAP
import imaplib
import time
import email
import datetime
from datetime import date as d
import re

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload().rsplit('\r\n', 2)[0]
    

user='sarikaspawar'
pwd='Saransh2017'
imap_url='imap.gmail.com'
mail=imaplib.IMAP4_SSL(imap_url)
mail.login(user,pwd)
mail.select('INBOX')
from_date=d.today()
to_date=from_date-datetime.timedelta(days=1)
to_date1=to_date.strftime("%d-%b-%Y")
#search gives only one item in list. 
type,data=mail.search(None, '(SENTSINCE {0})'.format(to_date1))
mail_ids=data[0]
id_list=data[0].split()
email_list=[]
first_email_id=int(id_list[0])
latest_email_id=int(id_list[-1])
num_of_emails=0
for i in range(latest_email_id,first_email_id, -1): 
    result, data = mail.fetch(str(i), "(RFC822)")
    for response_part in data:
         if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                emailDate = msg["Date"]
                mail_from = msg['from']
                sender = msg['from'].split()[-1]
                address = re.sub(r'[<>]','',sender)
                email_subject = msg['subject']
                emailid = re.split('@',address)
                user_id=emailid[0]
                domain=emailid[1]
                print("Received on: "+emailDate)
                print('From : ' + mail_from) 
                print("User_id: "+user_id)
                print("Domain ID: "+domain)
                if(email_subject!=None):
                    print('Subject : ' + email_subject)      
                else:
                    print('Subject : ' + "No Subject for this email")
                raw_email=data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                msg=email.message_from_string(raw_email_string)
                print(get_body(msg))
                print('\n')  
    num_of_emails=num_of_emails+1
    email_list.append(address)
    if(num_of_emails==5):
        break


# In[ ]:




