#Program that runs the Collatz conjecture loop
#Collatz practice
#
#Author : Alan Dineen


def collatz(number):
    if (number % 2 == 0):
        return number // 2
    elif (number % 2 ==1):
        return number * 3 + 1
    else:
        print("Something went wrong in Collatz")
        return None 
    
print("Please enter a number : ")
number = int(input())
print("The Collatzs Sequence is: ")
print(number)
while (number!= 1):
     number = collatz(number)
     print(number)

print(number)
