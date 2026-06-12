import requests  # 특정 URL 에 웹페이지(HTML) 정보를 요청하는 패키지
from bs4 import BeautifulSoup # 웹페이지 정보를 파이썬 객체화해서 파싱할수 있게 지원해주는 패키지
# bs4 패키지 안에 BeautifulSoup 클래스만  가져와!!
import re  # 정규표현식


url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%B0%98%EB%8F%84%EC%B2%B4'  # 웹페이지 요청할 URL 정보
#
# 💡 Header 정보 추가: 브라우저에서 요청한 것처럼 User-Agent 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 💡 requests.get 호출 시 headers 파라미터 추가
r = requests.get(url, headers=headers)
html = r.content  # 웹페이지 형태
#print(html)
# #
soup = BeautifulSoup(html, 'lxml')  # 파서 지정
newtilelist = soup.find_all(class_ = "sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1")
#print(newtilelist[0].text)
newdatalist = [  item.text  for item in newtilelist ]
print(newdatalist)
import pandas as pd
newsdf = pd.DataFrame(newdatalist, columns=["뉴스 제목"])
print(newsdf)

newsdf.to_excel("navernews.xlsx", index=False) # 엑셀파일 저장