#Program that runs the Collatz conjecture loop
#collatz,py
#Author : Alan Dineen

#Define collatz as x
def collatz(x):
    while x != 1:
        if x % 2 > 0:
             x =((3 * x) + 1)
             list_.append(x)
        else:
            x = (x / 2)
            list_.append(x)
    return list_
#Prompt user to input a number. to end the program they will enter a " "
print('Please enter a number: ', end='')
while True:
    try:
        x = int(input())
        list_ = [x]
        break
    except ValueError:
        print('Invaid selection, try again: ', end='')

l = collatz(x)
#Print out all the numbers it took to complete
print('\nList:', l, sep=' ')
#print('Number of steps required:', len(l) - 1)

