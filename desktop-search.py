import os
import re
import glob
userinput=input("Please enter file name to be searched: ")
dirlist=os.listdir("C:\\Users\\VPrakas\\Desktop\\CRs")
#print(dirlist)
a=glob.iglob("C:\\Users\\VPrakas\\Desktop\\**", recursive=True)
for i in a:
    if (re.search("%s" % userinput, i, re.IGNORECASE)):
        print (i)
input("Hit enter to exit")
