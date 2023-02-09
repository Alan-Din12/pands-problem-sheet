# accounts.py
# Author : Alan Dineen
# This is a program that reads a 10 character accunt number and outputs the account number with only
# the last 4 digits showing with the first 6 being displayed as "XXXXXX"

account = input("Please enter your 10 digit account number: ")

print(" XXXXXX" + account[6:])