from bs4 import BeautifulSoup as soup
import requests
import datetime
link='https://www.firstpost.com/sports/fifa-world-cup-2018-full-schedule-match-time-table-in-ist-venues-with-complete-fixtures-for-the-showpiece-tournament-in-russia-4491139.html'
html_frmt=requests.get(link)
bs_frmt=soup(html_frmt.content,"html.parser")
mydate = datetime.datetime.now()
today=mydate.strftime("%d %B")
a=bs_frmt.findAll("p")
length=len(a)
for i in range(4, length-61):
    b = a[i].text.splitlines()
    print(b,end='\n\n')
input("hit enter to exit")



