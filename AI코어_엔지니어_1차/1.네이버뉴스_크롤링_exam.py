import requests
from bs4 import BeautifulSoup
import re


url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query=%EB%B0%98%EB%8F%84%EC%B2%B4&oquery=%EB%A0%8C%ED%84%B0%EC%B9%B4&tqi=il5azlqo1e8ssUMT%2F%2BRssssssE4-287904'

r = requests.get(url, verify=False)  # 웹페이지 요청
html = r.content  # r.content Or r.text : 웹페이지 형태

soup = BeautifulSoup(html, 'lxml')  # 파서 지정

# 위 방법과 다른 find_all(), find() 메서드 활용
newtitlesoup = soup.find_all(class_ = 'news_tit')
