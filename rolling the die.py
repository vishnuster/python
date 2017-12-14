import random
import re
print(random.randint(0,6))
while True:
    a=input("Do you want to role again?")
    if (a.lower() == "yes"):
        print(random.randint(0,6))
        continue
    elif (a.lower() == "no"):
        break
    else:
        print("please enter a valid input")
        continue 
    
