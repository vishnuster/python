import platform
a=[platform.uname()]
for i in a:
    b=str(i)
    if('windows' in b.lower()):
        print(i[0],i[2],i[4],i[5])
    elif('linux' in b.lower()):
        print(i[1],i[4])
