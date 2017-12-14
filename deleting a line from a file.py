with open ('C:\\Users\\VPrakas\\Desktop\\python\\os_check.py','r') as file1:
    content=file1.readlines()
    for i in content:
        if ('this is a test' in i.lower()):
            continue
        else:
            with open ('C:\\Users\\VPrakas\\Desktop\\python\\os_testcheck.py','a') as file2:
                file2.write(i)
        
        
            
            
