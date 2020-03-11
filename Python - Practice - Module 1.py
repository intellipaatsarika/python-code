#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#variables
x=1000              
name='sarika'       #variable name with string literal in single quote
Name="pawar"        #variable name with string literal in double quote
salary =1000.14
print(Name)   
print(salary)
print(x)
print (name)
#Data types
print (type(x))          #Data types int, float, string
print (type(name))
print (type(salary))


# In[ ]:


a=100              #assignment operators
b=a*5             #arithmetic operators
c=a+b
c+=5               #assignment operators
home=None        # keyword same as NULL, it is special liberal
print (c)
print(3**4)       #exponential - 3^4
print(home)
print (a>b and c>b)   # comparision with logical operators
print (a>b or c>b)
print (b>a and c>b)


# In[ ]:


x=y=z=50
a,b,c = 10, 20 , 30 #mutli value assignment
print (x)
print (y)
print (z)
print (a)
print (b)
print (c)
print (x>a)        # Comparision operator
print (x is 50)   #identity operator
print (a is not 10)


# In[ ]:


multiline = '''line 1
line 2
line 3
line 4
line 5 '''
print (multiline)
a="""line a,
lineb
dfds
fsdf
dsfsd"""
print(a)


# In[ ]:


a = 1111111111111111111111111111111111111111111111.00000111111111
# value of integer is not restricted in bits it depends on memory
print (a)


# In[ ]:


print (7|5)  #bitwise operators
print (7&5)
print (~7)
print (~5)
print (10 >>1)  # 1010 >> 01010 >> 0101
print (10<<2)   # 101000


# In[ ]:


pets=['dog','cat','wolf']   # membership operator in, not in. these are used to find values from tuples, list etc.
print ('lion' in pets)
print ('cat' in pets)
print ('lion' not in pets)
if "tiger" in pets:
    print("tiger is not in pets")
elif "cat" in pets:
    print("cat in pets")


# In[ ]:


#Data structure types - Immutable ->>> Numbers, string and Tuples
#Mutable --> Lists, Dictionaries and Sets
#String data type  ---- Immutable data type
name ='sarika'
a="  pawar  "
str = 'word1-word2-word3'
print (a.strip())   #removes any whitespace from the beginning or the end
print (name [0])       #index returns character of that index
print (name [-1])       #returns last character of string
print (name[1:4])        #slicing from starting of string
print(name[-4:-1])       #slicing from end of the string
print (name.find('ri'))  #search for specified string and returns position of string
print (name.index('ri'))  #same as find
print (name.replace('ika','ansh'))   # replace first string with second
print (name.split('a'))         #split string with given separator in bracket
print (str.split('-'))
print (name.count('A'))    #Returns the number of times a specified value occurs in a string
print (str.count('wo'))    
print (name.upper())         #converts string to upper case
print (name.lower())         #converts string to lower case
print (max(name))        #max and min of ASCII value
print (min(name))
#concatenating string and with variable in print statement
print ("x is",x)   
print("Name is",name)
print("my salary is",salary ,"my age",x)


# In[ ]:


#concatenate string and string variables with +
name='Saransh'
Name='Adhav'
age = 2
weight = 11.2
FName=name+" "+Name
Address='Pune'
print(FName)
#Details="My Age " + age -   we cannot combine strings and numbers like this
Details="My Age: {}, Address: "+Address +", My Weight: {}"
print (Details.format(age,weight))
print("My Age: "+str(age)+", Address: "+Address+", My weight: "+str(weight))  #can use casting to combine string and int
DetailswithIndex="My Age: {1}, Address: {0}, My weight: {2}"  #Indexing arguments
print (DetailswithIndex.format(Address,age,weight))
print ("My name is \"Sarika Pawar\"")  #The escape character \ allows you to use double quotes
print('My son name is \'Saransh\'')


# In[67]:


#Python collection (arrays) - Tuple, lists, dictionaries, sets
# Tuples ---immutable - is a collection which is ordered and unchangeable. Allows duplicate members.
mytuple = ('ab','cd', 50, 100, 20)
mytuple1 =(1,2,3,4)
print (mytuple*2)         #Repetition - duplicate string by given no. of times
print (mytuple[2])         #indexing - gives data of given index
print (mytuple[1:3])     #slicing - gives specific set of string
mytuple+=mytuple1         #concatenation
print (mytuple)
#mytuple[2]=99       #tuple items are unchangeable
joecar=tuple('BMW')
print(joecar)


# In[ ]:


#List   --mutable --is a collection which is ordered and changeable. Allows duplicate members.
myList = ['abc','xyz', 100, 500, 666,'sarika',999]
print(myList)
myList.remove ('abc')    #removes element from List
myList.pop(2)       #remove element of mentioned index. or the last item if index is not specified
del myList[4]      #remove element of mentioned index.
print(myList)            
print (myList*2)           #repetition
print (myList[1:4])         #slicing
print (myList[-4:-1])
myList.append('pqr')        #append list with new value
print (myList)               
myList.insert(4,'abc')         #insert element at particular index
print (myList) 
myList[3]='Pawar'         #List is changeable
myList1 = [1,2,3]
myList+=myList1               #concatenation
print (myList) 
myList.extend(myList1)      #extend same as concatenaion. what is difference?
print (myList)
print (myList[0])
print (myList[-1])
print(myList)
newList=myList.copy()      # make a copy of list using copy method
print(newList)
List1=list(newList)       #make copy of list using list method 
list= "List1: {}"
print (list.format(List1))       
myList.clear()  
print(myList)       #empties the lists
del myList                #delete the list completely


# In[62]:


#Dictionaries--- key value pair -- Mutable - is a collection which is unordered, changeable and indexed. No duplicate members.
myDict = {}     # empty dictionary
myDict1 ={1:'a',2:'b',3:'c',4:'d'}     # integer keys
myDict2={'name':'sarika', 2:'pawar'}       #mixed keys
print (myDict1.keys())          # fetch all keys of dictionary
print (myDict2.values())        # values
print (len(myDict1))          #No. of pairs in dictionary
print (myDict2['name'])       # access values by proving keys
for d in myDict1:
    print(d,end=":")
    print(myDict1[d])


# In[ ]:


#Sets  --  is a collection which is unordered and unindexed. No duplicate members.
#indexing not possible
mySet1= {1,2,'sarika',12.5}
mySet2 = {1,32,'sarika',22.5}
print (mySet1|mySet2)       # Union - give unique values from whole list
print (mySet1&mySet2)       #Intersection - only common vales from both lists
print (mySet1-mySet2)        #Difference - gives unique values from first set which are not in second set
for x in mySet1:
    print(x)
mySet1.add("Pawar")
print(mySet1)
mySet1.update("S")
print(mySet1)
print(len(mySet1))
mySet1.remove(12.5)
print(mySet1)


# In[ ]:


#Flow control in python
# If-else, Nested if-else, for, while, break, continue
a=10
b=100
if a>b:
    print ('a is greater than b')          #take care of indentation 
elif a==b:
    print('a equal to b')
else:
    print ('a is less than b')


# In[ ]:


#for loop - iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
for x in "banana":
    print (x,end=",")
    if (x=='n'):
        break                  # break statement we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if(x=='banana'):
        break
    print(x)
AGE= [56,78,89,70]
for x in AGE:
    if(x==89):
         continue           #continue statement we can stop the current iteration of the loop, and continue with the next
    print(x)
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
else:
    print("for loop finished for age") 

#Nested for loop with break and continue
adj =['red','yellow','tasty']
fruits=['watermelon','papaya','banana']
for x in fruits:
    #print(x)
    for y in adj:
     #   print(y)
        if(x=='watermelon'and y=='yellow'):
            continue
        if(x=='banana'and y=="red"):
            break
        print (x,y)


# In[ ]:


"""for loop with range() function
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
and ends at a specified number
ex. of multiline comment
"""
for x in range(6):     #Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
    print(x,end=",")
print()
for x in range (2,6):    #starting value of count value is 2 here. so loop for 2 to 5.
    print (x,end=",")
print()
for x in range (3,18,4): # starting value(default is 1), range, increment by (default is 1)
    print(x,end=",")
print()
for x in range (18,6,-4): # starting value(default is 1), range, decrease by (default is increase by 1)
    print(x,end=",")
else:
    print ('\nfor loop finished')


# In[ ]:


#if else, for loop can not be empty means it shold have some statements. for empty loop use 'pass' to avoid errors
a=5
b=5
if (a==b):
    pass      #no statement to execute
for x in [1,2,3]:
    pass       #no statement to execute
def myfunction():
    pass        #no statement to execute


# In[ ]:


#while loop
i=0
while(i<=5):
    print(i)
    i+=1
else:
    print("i no longer matching condtion")

#else statement we can run a block of code once when the condition no longer is true


# In[ ]:


#A function is a block of code which only runs when it is called. You can pass data, known as parameters/arguments,
#into a function.A function can return data as a result.
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that are sent to the function when it is called.

def myFunction():
    print("My first function in Python")
myFunction()
 
#function returns a value with the return statement
def arithmetic(num1,num2):             #parameters
    result1=num1*num2
    print(num1,"*",num2,"=",result1)
    return result1
result=arithmetic(4,2)                            #arguments
print("value returned",result)

#-Arbitrary Arguments, *args --- If the number of arguments is unknown, add a * before the parameter name 
def arbFunction(*parm): 
    print(parm)
    print(parm[1])           #using 0,1,..n to get arbitary aruguments
arbFunction(1,2,3,"Sarika")

#Keyword arguments - kwargs -send arguments with the key = value syntax. parameters name and argumnent's key name should be same
def fun_keyvalue(parm1,parm2,parm3):
    print("values: "+parm1)
fun_keyvalue(parm1 = "Emil", parm2 = "Tobias", parm3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs
def arbKeyFn(**name):
    print("My name is "+name['fname']+" "+name['lname'])       #using key names to get arbitary arguments.
arbKeyFn(fname="sarika",lname="pawar")

#Default Parameter Value -  If we call the function without argument, it uses the default value
def defValFunction(country='India'):
    print(country)
defValFunction('New York')
defValFunction()

#pass list as an argument
def listFunction(food):
    for x in food:
        print(x)
fruits =["orange","apple","banana"]
listFunction(fruits)


# In[ ]:


#try global and local variable with functions
i=10                #global variables that are created outside of a function which we can use inside and outside function
j=16
def myFuntion(i):
    i=6            # using local variable inside function
    global k       # use the global keyword, the variable belongs to the global scope
    k=70
    print(i)
    print(j)
myFuntion(i)
print(k)

#Recursion - a function calls itself.   TRY LATER
def tri_recursion(k):
    #print(k)
    if(k > 0):
       # print(k)
        result = k + tri_recursion(k - 1)
        print("print",result)            #when this statement exactly running?
    else:
        result = 0
        print("else")
    return result

print("\n\nRecursion Example Results")
n=tri_recursion(6)
print("returned:",n)


# In[ ]:


def computeAffected(n):
    newly_affected=1
    total_affected=1
    for day in (2,n+1):
        print("before:"+str(total_affected))
        newly_affected=newly_affected*2
        total_affected=total_affected+newly_affected
        print("after:"+str(total_affected))

    print(total_affected)

computeAffected(3)


# In[ ]:


Name=input("Enter Name: ")  #it provide text box to give input
print(Name)


# In[ ]:


#pass by val and pass by ref..pending with Joe
def fun(b):
    b=10
    return b

a=5
print(fun(a))
print (a)

def funRef(List):
    List=[1,2]
    return List

list=[0]
print(funRef(list))
print (list)


# In[ ]:


#A lambda function can take any number of arguments, but can only have one expression.
#Use lambda functions when an anonymous function is required for a short period of time.

x=lambda a:a*10   # x is name of lambda function
print(x(5))

def myFun(a):
    return lambda b:b*a
mydouble=myFun(2)
print(mydouble(11))


# In[6]:


#function returning multiple values using collection i.e. tuple, lists, dictionaries
def myFun(a,b):
    return (a*b,a+b,"sarika")

tuple_ex=myFun(2,3)
print(tuple_ex)

#list ex.
def myFun(a,b):
    return [a*b,a+b,"sarika"]

lists=myFun(2,3)
print(lists)

#use objects to 


# In[48]:


#file handling
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist- will append to the end of the file
#"w" - Write - will create a file if the specified file does not exist - will overwrite any existing content
import os
f=open("E:/Intellipaat/rwac1.txt","w")
f=open("E:/Intellipaat/rwac1.txt","w")
f.write("This is first line")
f.close()
f=open("E:/Intellipaat/rwac1.txt","r")
print("After 1st write")
print(f.read())
f.close()
f=open("E:/Intellipaat/rwac1.txt","a")
f.write("   This is appended line")
f.close()
f=open("E:/Intellipaat/rwac1.txt","r")
print("After append")
for x in f:
    print(x)
f.close()
f=open("E:/Intellipaat/rwac1.txt","w")
f.write("Old data overwritten by new")
f.close()
f=open("E:/Intellipaat/rwac1.txt","r")
print("After 2nd write")
print(f.read())
f.close()
if os.path.exists("E:/Intellipaat/rwac1.txt"):
    os.remove("E:/Intellipaat/rwac1.txt")
    print("file deleted")
else:
    print("The file does not exist")
    
#os.rmdir("myfolder")         #can only remove empty folders.


# In[65]:


import os
print(os.getcwd())
print(os.getlogin())
print(os.listdir())


# In[113]:


#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

import re
txt="My Name is Sarika"
x=re.search("ka$",txt)
print(x)
print(x.span())               #span=
print(x.string)             #whole string
print(x.group())            #match= means mathing string
if(x):
    print("String matched")
else:
    print("No match")

print(re.findall("a",txt))
print(re.sub("\s","-",txt))          #replaces the matches with the text of your choice
print(re.sub("\s","-",txt,2))        #control the number of replacements by specifying the count
print(re.split("\s",txt))
print(re.split("\s",txt,1))

