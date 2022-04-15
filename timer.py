import time
from os import system,name
while True:
    ch = input("are you ready (y/n): ")
    if "y" in ch.lower():
        h = int(input("enter hour: "))
        m = int(input("enter minute: "))
        s = int(input("enter secound: "))
        t = h * 3600 + m * 60 + s
        print("timer start... ")
        time.sleep(1)
        
        while t>=1:
            print(t)
            t -=1
            time.sleep(1)
            
            if name =="nt":
                system("cls")
            else: 
                system("clear")
        print("timer ended...!")
    elif "n" in ch.lower():
        print("good bay....")
        break
    else:
        print("inValid input....")