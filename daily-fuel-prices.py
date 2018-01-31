#Daily fuel prices across all metros
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
link="https://www.iocl.com/TotalProductList.aspx"
html_frmt=urlopen(link)
bs_frmt=soup(html_frmt,"html.parser")
a=bs_frmt.findAll("div",{"class":"product-table-section"})
b=a[0].text.replace("Previous Prices","").splitlines()
c=a[0].text.replace("Previous Prices","").split()
print(b[1],end="\n")
print(b[4],end="\n\n")
print(c[18],end="\t");print(c[19])
print(c[20],end="\t");print(c[21])
print(c[22],end="\t");print(c[23])
print(c[24],end="\t");print(c[25],end="\n\n")
diesel=a[3].text.splitlines()
diesel2=a[3].text.split()
usr=str(input("Type diesel if you want diesel prices or hit enter to exit: "));print("\n")
if(usr == "diesel"):
    print(diesel[1],end="\n");print(diesel[4],end="\n\n")
    print(diesel2[18],end="\t");print(diesel2[19])
    print(diesel2[20],end="\t");print(diesel2[21])
    print(diesel2[22],end="\t");print(diesel2[23])
    print(diesel2[24],end="\t");print(diesel2[25])
else:
    exit()
input()
