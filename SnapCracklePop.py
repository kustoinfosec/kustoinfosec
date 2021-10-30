"""This module will print the numbers 1-100. If the number is divisible by 3,
Crackle will print instead. If the number is divisible by 5, Pop will print instead."""

def display(n):
    for i in range(1,n):
        if i%10 == 0:
            print()
        if i%5 == 0:
            print(i,"Snap",end = ",")
        elif i%7 == 0:
            print(i,"Pop",end = ",")
        else:
            print(i,end = ",")

     if n%10 == 0:
         print()
     if n%3 == 0:
         print(n,"Snap",end = "")
     elif n%5 == 0:
         print(n,"Crackle",end = "")
     elif n%7 == 0:
         print(n,"Pop",end = "")
     else:
         print(n,end = "")

display(100)

def display(snap,crackle,pop,n):
    for i in range(1,n):
        if i%10 == 0:
            print()
        if i%snap == 0:
            print(n,"Snap",end = "")
        elif i%pop == 0:
            print(n,"Pop",end = "")
        elif i%pop == 0:
            print(n,"Pop",end = "")
        else:
            print(n,end = "")



snap = input("Enter the value of snap: ")
if snap.isdigit() == False:
    print("Value must be an integer")
    snap = input("Enter the value of snap: ")
if int(snap) <= 0:
    print("Value must be positive")
    snap = input("Enter the value of snap: ")


    
crackle = input("Enter the value of crackle: ")
if crackle.isdigit() == False:
    print("Value must be an integer")
    crackle = input("Enter the value of snap: ")
if int(crackle) <= 0:
    print("Value must be positive")
    crackle = input("Enter the value of snap: ")


    
snap = input("Enter the value of pop: ")
if pop.isdigit() == False:
    print("Value must be an integer")
    pop = input("Enter the value of snap: ")
if int(pop) <= 0:
    print("Value must be positive")
    pop = input("Enter the value of snap: ")



display(int(snap),int(crackle),int(pop),100
    
    





            
        
