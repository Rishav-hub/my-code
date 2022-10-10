# This is a scrapping project
import pandas
from bs4 import BeautifulSoup
import requests
list=[]
r = requests.get("https://en.wikipedia.org/wiki/List_of_Britain%27s_Got_Talent_finalists", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("table",{"class":"wikitable sortable jquery-tablesorter"})
print(soup.prettify())
