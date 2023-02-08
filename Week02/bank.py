#bank.py
#Author: Alan Dineen
#This program prints out a sum of money in euro and cents. 

amount1 = int(input("Enter the first amount in cents: "))
amount2 = int(input ("Enter the second amount in cents: "))
sum = amount1 + amount2
total = int(sum)/100
print (f"The sum of these is €{total}")
