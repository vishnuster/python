import os
import docx2txt
import time
os.chdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
a=os.listdir('C:\\Users\\vprakas\\Desktop\\python\\kpi')
#fullText=[]
for i in a:
    try:
        b = i.split("_")
        cc = b[0]
        print(cc)
        text = docx2txt.process(i)
        b=text.splitlines()
    #print(b)
        for x in range(len(b)):
            if "Maintenance Window" in b[x]:
                changetime=str(b[x+2:x+3])
                print(changetime)
            if "Affected Devices" in b[x]:
                for z in b[x:x+2]:
                    q=z
                    servername=q.replace("Affected Devices:","")
                    print(servername)
        print("*"*100)
    except:
        pass






