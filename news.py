import requests
from bs4 import BeautifulSoup as soup
url='https://timesofindia.indiatimes.com/'
ht=requests.get(url)
bs=soup(ht.content,'html.parser')
a=bs.find_all('div',{'class':'top-story'})
b=str(a[0].text)
print(b)
latest=((bs.find_all('div',{'class':'widget'})))
c=str(latest[0].text)
d=c.splitlines()
e=len(d)
for i in range(1,e-6):
    print(d[i])
input("hit enter to exit")

