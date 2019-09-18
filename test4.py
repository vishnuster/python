import os
import docx2txt
import time
os.chdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
a=os.listdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
#fullText=[]
for i in a:
    try:
        #print(i)
        text = docx2txt.process(i)
        b=text.splitlines()
        for x in range(len(b)):
            if "Maintenance Window" in b[x]:

                for z in b[x+2:x+5]:
                    print(z)
            if "Affected Devices" in b[x]:

                for z in b[x:x+4]:
                    print(z,end="|")
        #print("*"*100)
    except:
        print("doc file instead of docx file.",i.capitalize())