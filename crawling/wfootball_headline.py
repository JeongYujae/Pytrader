from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#해외축구 인기순 뉴스 url
url='https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=popular'

def wfootball_headline(n): #Number of headline
    html = urlopen(url).read() #Get info from url
    headline_list=[]
    soup = BeautifulSoup(html,'html.parser')
    title_html = soup.select('.title>span')
    for i in range(n):
        a=title_html[i].text
        print(a.strip())
wfootball_headline(10)





