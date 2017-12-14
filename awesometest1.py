import os
import re
import shutil
while True:
    userinpt=input("enter folder name to be created: ")
    check=os.path.isdir("C:\\Users\\VPrakas\\Desktop\\%s" % userinpt)
    if (check != True):
        os.chdir("C:\\Users\\VPrakas\\Desktop")
        os.mkdir("%s" %userinpt)
        print(userinpt, "folder created")
        break
    else:
        print("Folder already created. Enter some other name")
        continue
#os.chdir("C:\\Users\\VPrakas\\Desktop\\%s" %userinpt)
for i in range(10):
    with open("C:\\Users\\VPrakas\\Desktop\\%s\\file-%s.txt" %(userinpt,i), 'w') as test:
        test.write("this is a test file with the name file-%s.txt" %i)

while True:
    del1=input("enter folder name to be deleted or hit 1 to exit: ")
    if (del1 == "1"):
        break
    else:
        yesno=str(input("Do u really want to delete %s? yes/no" %del1))
        if (yesno == "yes"):
            shutil.rmtree("%s" %del1)
        elif (yesno == "no"):
            exit
        else:
            print("type yes or no")
        continue


    


        
        
