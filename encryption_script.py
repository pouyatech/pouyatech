#python code with pouya
while True:
    print("choose your option: \n \t 1)encrypt \n\t 2)decript \n\t 3)Exit \n")
    choice = input("your choice: ")
    
    if choice == "1":
        plant = input("text: ")
        entext = ""
        for c in plant:
            x = ord(c) *3 +2 -1
            entext += chr(x)
        print("encrypted text:" ,entext ,"\n")
        print("*" * 40 + "\n"  )
        
    elif choice =="2":
        plant = input("dec text: ")
        entext = ""
        for c in plant:
            x = ((ord(c) +1) -2 ) // 3
            entext += chr(x)
        print("encrypted text:" ,entext ,"\n")
        print("*" * 40 + "\n"  )
       


    elif choice =="3":
        print("good bay!")
        break
    else: 
        print("your choice is wrong!!! \n")
    
    
