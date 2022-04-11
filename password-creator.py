#made by pouya

import random
import string


lw = string.ascii_lowercase
uw = string.ascii_uppercase
sym = "~!@#$%^&*()_+|:?><>"
num = "123456789"
all= lw + uw + sym + num

while True:
  print("choose: \n \t 1)creat password  \n \t 2) Exit" )
  choice = input("your choice: ")
  if choice == "1":
    le = int(input("enter lenght of password: "))
    passw = "".join((random.sample(all , le)))
    print("your password:", passw + "\n")

  elif choice == "2":
    print("good bay!! \n this script made by pouya \n\n")
    break
  else:
    print("enter corect number!! \n")

