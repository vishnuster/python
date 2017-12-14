import os
import re
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
link='https://www.iocl.com/TotalProductList.aspx'
html_frmt=urlopen(link)
bs_frmt=soup(html_frmt,"html.parser")
a=(bs_frmt.findAll("div", {"class":"tableScroll"}))
actual=a[0].text
b=actual.splitlines()
c=b[21].replace('Panjim','')
today=time.strftime("%d/%m/%Y")
print("Petrol price in Panjim on", today,"is",c,"\n")
input("Hit enter to exit")
    

