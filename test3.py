import os
import docx2txt
import time
os.chdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
a=os.listdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
#fullText=[]
for i in a:
    try:
        print(i)
        text = docx2txt.process(i)
        b=text.splitlines()
    #print(b)
        for x in range(len(b)):
            if "Maintenance Window" in b[x]:
                print(b[x+2:x+5])
        print("*"*100)
    except:
        pass






