# accounts.py
# Author : Alan Dineen
# This is a program that reads a 10 character accunt number and outputs the account number with only
# the last 4 digits showing with the first 6 being displayed as "XXXXXX"

#account = input("Please enter your 10 digit account number: ")
#Here I added 6 X's t block out the first 6 numbers of the bank number. 
#print(" XXXXXX" + account[6:])

#To change the problem to only show the last 4 digits of any length number I used the following code
account2 = input("Please enter your  account number: ")

print ( account2[-4:])


