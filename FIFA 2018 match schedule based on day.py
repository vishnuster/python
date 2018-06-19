from bs4 import BeautifulSoup as soup
import requests
import datetime
import os
mydate = datetime.datetime.now()
today=mydate.strftime("%d %B")
#today='16 June'
t=today.split()
link='https://www.firstpost.com/sports/fifa-world-cup-2018-full-schedule-match-time-table-in-ist-venues-with-complete-fixtures-for-the-showpiece-tournament-in-russia-4491139.html'
html_frmt=requests.get(link)
bs_frmt=soup(html_frmt.content,"html.parser")
a=bs_frmt.findAll("p")
length=len(a)
for i in range(4,length-61):
    if (today in a[i].text):
        for j in range(4):
            print(a[i+j].text)
#usr=str(input("Type 'all' to list all matches: "))
#if (usr == 'all'):
#    exec('C:\\Users\\vprakas\\Desktop\\python\\FIFA_2018_matches')
    #os.system('python3 C:\\Users\\vprakas\\Desktop\\python\\FIFA_2018_matches.py')
input("\n Hit enter to exit")


