import requests # 특정 url의 웹페이지(html)정보를 요청하는 패키지
from bs4 import BeautifulSoup   # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# bs4 패키지 안에서 BeautifulSoup 클래스만 가져와~
import re


url = 'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%B0%98%EB%8F%84%EC%B2%B4' # html 정보 요청할 url
r = requests.get(url)  # 웹페이지 요청
html = r.text  # r.content (바이트로 가져옴  Or r.text (문자열로 가져옴)
print(html)

soup = BeautifulSoup(html, 'lxml')  # 파서 지정
#html.parser보다 lxml은 파싱할 때의 속도가 빠름!
# but, 이건 내장된 게 아니라 pip install로 깔아야 함

# 위 방법과 다른 find_all(), find() 메서드 활용
# newtitlesoup = soup.find_all(class_ = 'news_tit')
