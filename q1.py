# write a python program to input a positive integer , Display 
# correct massage for correct and incorrect massage

a1=input("enter the number \n")
try:
    a=int(a1)
    if a>0:
        print("this is a positive integer ")
    else:
        print("this is not a positive integer ")
except ValueError:
    print("enter the positive integer ")