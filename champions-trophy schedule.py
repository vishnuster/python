from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
ct='https://www.icc-cricket.com/champions-trophy/fixtures'
ht_frmt=urlopen(ct)
bs_frmt=soup(ht_frmt.read(),'html.parser')
content=bs_frmt.findAll('div',{'class':'match-block__team-container'})
userinp=str.capitalize(input("Type 'India' to get India specific matches. Else type 'all' to get all match schedules: "))
a=0
for match_date in content:
    match_date=(content[a].div.text)
    summary=bs_frmt.findAll('div',{'class':'match-block__summary'})
    vs=content[a].findAll('div',{'class':'match-block__team'})
    vs_other=vs[1].text
    if ("%s" %userinp in str(vs)):
        print(vs[0].text);print("Vs");print(vs_other)
        print(match_date)
        print(summary[a].text.strip())
        print("===========================================================================\n")
    elif("%s" %userinp in str(vs_other)):
        print(vs[0].text);print("Vs");print(vs_other)
        print(match_date)
        print(summary[a].text.strip())
        print("===========================================================================\n")
    elif("%s" %userinp == "All"):
        print(vs[0].text);print("Vs");print(vs_other)
        print(match_date)
        print(summary[a].text.strip())
        print("===========================================================================\n")
    else:
        exit
    a=a+1
input("hit enter to exit")



