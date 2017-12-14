with open('C:\\Users\\VPrakas\\Desktop\\test.txt',"r") as content_file:
    content=content_file.read().lower().splitlines()
a=0
for i in content:
        if("maintenance window" in i):
            print(i)
        elif("change control" in i):
            print(i)
