from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
cricbuzz='http://www.cricbuzz.com/cricket-match/live-scores'
ht_frmt=urlopen(cricbuzz)
bs_frmt=soup(ht_frmt,'html.parser')
score=bs_frmt.findAll("div", {"class": "cb-col cb-col-100 cb-lv-main"})
#print(score[0].text)
banner=score[0].h2.text
print(banner)
banner2=score[0].h3.text
print(banner2.replace(',',""))
a=bs_frmt.findAll("div", {"class": "cb-col-100 cb-col cb-schdl"})
score_board=(a[1].a.text)
print(score_board.strip())
input("hit enter to exit")
