import os
import re
userinp=input("enter file name to be searched: ")
walk=os.walk("C:\\Users\\VPrakas\\Desktop")
print("Patterns that match", userinp,"are given below\n")
for path, folder, files in walk:
    for i in files:
        if(re.search('%s' %userinp, i,re.IGNORECASE)):
           print(path,folder,i)
input("hit enter to exit")
