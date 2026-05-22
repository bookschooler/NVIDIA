import requests # 특정 url의 웹페이지(html)정보를 요청하는 패키지
from bs4 import BeautifulSoup   # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# bs4 패키지 안에서 BeautifulSoup 클래스만 가져와~
import re

url = 'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%B0%98%EB%8F%84%EC%B2%B4' # html 정보 요청할 url
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers, timeout=10)  # 웹페이지 요청
html = r.content  # r.content (바이트로 가져옴  Or r.text (문자열로 가져옴)
# print(html)

soup = BeautifulSoup(html, 'lxml')  # 파서 지정
newstitlelist = soup.find_all(class_='sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1')
# print(newstitlelist[0])

newsdatalist = [ item.text for item in newstitlelist]
print(newsdatalist)

import pandas as pd
newsdf = pd.DataFrame(newsdatalist, columns=['뉴스 제목'])
print(newsdf)
newsdf.to_excel("navernews.xlsx", index=False)   # 엑셀파일 저장
