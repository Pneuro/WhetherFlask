import sys
import time
from pymongo import MongoClient
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver


client = MongoClient('mongodb://localhost:27017')
##############################################################################################
########################### Scraped Items ####################################################
##############################################################################################

# UNIVERSAL AUDIO APOLLO TWIN X DUO THUNDERBOLT 3 INTERFACE


url = 'https://www.musiciansfriend.com/pro-audio/universal-audio-apollo-twin-x-duo-thunderbolt-3-audio-interface/l69012000000000?rNtt=apollo&index=1'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
title = page_soup.find('title')
containers = page_soup.find('span', 'price-wrap')
clean = containers.text.strip()
cleanTitle = title.text.strip()
displayRes = 'The ' + cleanTitle + ' is going to cost ' + str(clean)
print(cleanTitle)
result = print('The ' + cleanTitle + ' is going to cost ' + str(clean))


# MARSHALL JVM SERIES JVM410H 100W TUBE GUITAR AMPLIFIER


urlAmp = 'https://www.musiciansfriend.com/amplifiers-effects/marshall-jvm-series-jvm410h-100w-tube-guitar-amp-head'
reqAmp = Request(urlAmp, headers={'User-Agent': 'Mozilla/5.0'})
webpageAmp = urlopen(reqAmp).read()
page_soup_Amp = soup(webpageAmp, "html.parser")
titleAmp = page_soup_Amp.find('title')
containersAmp = page_soup_Amp.find('span', 'price-wrap')
cleanAmp = containersAmp.text.strip()
cleanTitleAmp = titleAmp.text.strip()
displayResAmp = 'The ' + cleanTitleAmp + \
    ' is going to cost ' + str(cleanAmp)
print(cleanTitleAmp)
print('The ' + cleanTitleAmp + ' will cost ' + cleanAmp)


# Apple Watch

urlWatch = 'https://www.amazon.com/Apple-Watch-GPS-40mm-Aluminum/dp/B07XR5TRSZ/ref=sr_1_2_sspa?keywords=apple+watch&qid=1578007379&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQ0FGVjRKQzY1TDBTJmVuY3J5cHRlZElkPUEwOTU0ODg4M0lBT1ZFVkZMSlQ1MyZlbmNyeXB0ZWRBZElkPUEwMDg1NjAwMU5aSVFQNEtORTc0MSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
reqWatch = Request(urlWatch, headers={'User-Agent': 'Mozilla/5.0'})
webpageWatch = urlopen(reqWatch).read()
page_soup_Watch = soup(webpageWatch, "html.parser")
titleWatch = page_soup_Watch.find('title')
containersWatch = page_soup_Watch.find(
    'span', 'priceBlockBuyingPriceString')
cleanWatch = containersWatch.text.strip()
cleanTitleWatch = titleWatch.text.strip()
displayResWatch = 'The ' + cleanTitleWatch + \
    ' is going to cost ' + str(cleanWatch)
print(cleanTitleWatch)
print('The ' + cleanTitleWatch + ' in question will cost ' + cleanWatch)


##############################################################################################
########################### Interface ########################################################
##############################################################################################
