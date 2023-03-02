#Author : Alan Dineen
#This program outputs a message to let the user know if it is the weekend or not. 

#set your lists
a = ["Sat", "Sun"]
b = ["Mon","Tue","Wed","Thur","Fri"]



import datetime

x = datetime.datetime.now()
#get only the day in short form eg 'Mon'
y = (x.strftime("%a"))

#Create your if statement: 
if (y != a): 
    print ("Yes, unfortunately tday is a weekday")
else :
    print ("It is the weekend! Woohoo!!!")