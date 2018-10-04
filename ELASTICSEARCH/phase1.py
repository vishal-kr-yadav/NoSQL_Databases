from flask import Flask
from converterFromUnicode import convert
from connection import executeQuery
from connection import createDocument
from converterFromUnicode import convert
import urllib2
from bs4 import BeautifulSoup
import requests
import pandas as pd
import unicodedata
from connection import createDocument
from connection import createBackup


import re
app=Flask(__name__)

@app.route('/GET/Review/By/keywords/<keywords>', methods=['GET'])
def getReviewByKeywords(keywords):

    body = {"query": {"match": {'review': keywords}}}

    ok=convert(body)
    return executeQuery(ok)

@app.route('/PUT/Review/iphoneX/From/Amazon/<count>', methods=['GET'])
def putReviewforIphoneX(count):
    item=convert(count)
    intItem=int(item)
    print(intItem)
    list = []
    res = requests.get(
        "https://www.amazon.in/Apple-iPhone-Space-Grey-256GB/dp/B072LNNSQN/ref=sr_1_4?s=electronics&ie=UTF8&qid=1519143645&sr=1-4&keywords=iphone+x&dpID=41wUnHPGFBL&preST=_SY300_QL70_&dpSrc=srch")
    soup = BeautifulSoup(res.content, 'lxml')
    for each in soup.find_all('div', attrs={'class': 'a-section review'}):
        reviewData = unicodedata.normalize('NFKD', re.sub('\s+', ' ', each.text)).encode('ascii', 'ignore').split(':')
        list.append(reviewData[0])
    createDocument(list,intItem)
    # createBackup(0,intItem)
    return "Created"



if __name__ == '__main__':
    app.run(debug=True)
