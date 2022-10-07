import pandas
from bs4 import BeautifulSoup
import requests
list=[]
# Test from pavan
# test pavan 2
baseurl="https://www.flipkart.com/search?q=i%20phone%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
for page in range(1,4): ###This would crawl over various pages
    print(baseurl+str(page))
    r = requests.get(baseurl+str(page))
    c=r.content    #grab the content from the lin
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"_3O0U0u"}) #This contains all the information in list format

    for item in all:
        d={}
        d["NAME"]=item.find("div",{"class":"_3wU53n"}).text #Name of the phone
        d["PRICE"]=item.find("div",{"class":"_1vC4OE _2rQ-NK"}).text #price
        d["RATINGS"]=item.find("div",{"class":"hGSR34"}).text #ratings
        try:
            d["DISCOUNT"]=item.find("div",{"class":"VGWI6T"}).find("span").text #% of discount
        except:
            d["DISCOUNT"]="No discount"
        try:
            d["REVIEWS AND RATINGS"]=item.find("span",{"class":"_38sUEc"}).find("span").text.replace("\xa0&\xa0"," & ") #reviews and ratings in count
        except:
            d["REVIEWS AND RATINGS"]="No ratings ..New product"
        try:
            d["AVAILABILITY"]=item.find("div",{"class":"_3aV9Tq"}).find("span").text #availability
        except:
            d["AVAILABILITY"]="available"
        list.append(d)
    df=pandas.DataFrame(list)
    df.to_csv("Flipkart.csv") #generated a CSV file
