with open('C:\\Users\\VPrakas\\Desktop\\test.txt.txt',"r") as content_file:
    content=content_file.read()
lower1=content.lower()
if("compact" in lower1):
    print("CR for schema compacting")
elif("stop and start" in lower1):
    print("CR for stop/start")
else:
    exit
this is a test