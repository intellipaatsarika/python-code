#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python's client side library called imaplib is used for accessing emails over imap protocol.IMAP-Internet Mail Access Protocol.
#program to display all mailboxes of gmail, create new mailbox, delete existing mailbox.
#deleting all messages from spam folder

import imaplib

user='userid'
pwd='pwd'
imap_url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
#make sure gmail setting allow you to log in using IMAP
mail.login(user, password)
#list returns type and mail box data
typ,mailbox_data=mail.list()
#mailbox_data has flag, delimiter and mailbox_name  Ex. b'(\\HasNoChildren) "/" "INBOX"'
for line in mailbox_data:
    print(line)
mail.select('[Gmail]/Spam')
#SEARCH only returns one line, so you have a list of one item. so result stores in data[0]
typ,data=mail.search(None,'ALL')
#delete emails using store and expunge functions
if(len(data[0].split())>0):
    for num in data[0].split():
        mail.store(num,'+FLAGS','\\Deleted')
    mail.expunge()
    if(len(data[0].split())==1):
        print(len(data[0].split()),"spam message deleted")
    else:
        print(len(data[0].split()),"spam messages deleted")
else:
    print(len(data[0].split()), "spam message")
#mail.create('Practice')      #creating new mailbox
#mail.delete('Practice')     #deleting old mailbox
mail.close()
mail.logout()


# In[ ]:




