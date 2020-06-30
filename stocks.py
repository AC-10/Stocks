import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import time



#print(r.text)  will print the entire html docs


def curr_price(stock_code):
    #https://in.finance.yahoo.com/quote/AXISBANK.NS?p=AXISBANK.NS&.tsrc=fin-srch

    url = ("https://in.finance.yahoo.com/quote/")+stock_code+("?p=")+stock_code+("&.tsrc=fin-srch")
    r = requests.get(url)
    stock_details=BeautifulSoup(r.text,"lxml")
    stock_details=stock_details.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
    #The stock price is present within the span tag
    stock_details=stock_details.find("span")
    stock_price=stock_details.text

    #becoz of continuosly refreshing the data sometimes there may be no value present hence replce the price with 9999
    #which can be seen as an outlier and replace the value later
    if stock_price==[]:
        stock_price="9999"

    return stock_price


portfolio=["HDB","AXISBANK.NS","YESBANK.NS"]

for i in range(1,101):
    price=[]
    col=[]
    timestamp=datetime.datetime.now()
    timestamp=timestamp.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(60)
    for stock_code in portfolio:
        price.append(curr_price(stock_code))
    col=[timestamp]
    col.extend(price)  # combining price with the timestamp
    df=pd.DataFrame(col) # putting into a dataframe
    df=df.T   #Transforming the df from columns to rows
    df.to_csv("real time stock data.csv",mode="a",header=False)
    print(col)
