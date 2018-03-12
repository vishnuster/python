import requests
from bs4 import BeautifulSoup as soup
url='https://timesofindia.indiatimes.com/'
ht=requests.get(url)
bs=soup(ht.content,'html.parser')
#print(bs.prettify())
a=bs.find_all('div',{'class':'top-story'})
#a=bs.find_all('ul',{'class':'hd1'})
b=str(a[0].text)
for i in range(len(b.splitlines())):
    print(b.splitlines()[i])
latest=(bs.find_all('div',{'class':'widget'}))
c=(latest[0].text)
print(c)
input("hit enter to exit")