from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

toi='http://timesofindia.indiatimes.com/'

html_format=urlopen(toi)
bs_format=soup(html_format.read(),'html.parser')
content=bs_format.findAll('ul',{"class":"list8"})
abc=(content[0])
for abc in content:
    print(abc.li.a['title'])
