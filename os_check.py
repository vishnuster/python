import os
import platform
#print(platform.system(),platform.release())
a=platform.uname()
os=a[0]
flavour=a[1]
kernel=a[2]
inpt=str(input("Enter os, flavour or kernel:"))
lower=inpt.lower()
if (inpt == 'os'):
    print(os)
elif (inpt == 'flavour'):
    print(flavour)
elif (inpt == 'kernel'):
    print(kernel)
else:
    print("wrong input")
