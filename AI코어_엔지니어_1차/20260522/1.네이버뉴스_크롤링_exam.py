
import requests  # 특정 URL 에 웹페이지(HTML) 정보를 요청하는 패키지
from bs4 import BeautifulSoup # 웹페이지 정보를 파이썬 객체화해서 파싱할수 있게 지원해주는 패키지
# bs4 패키지 안에 BeautifulSoup 클래스만  가져와!!
import re  # 정규표현식


url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'  # 웹페이지 요청할 URL 정보
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
#
# # 위 방법과 다른 find_all(), find() 메서드 활용
newtitlesoup = soup.find_all('td', class_ = 'subject')  # 리스트로  반환
print(len(newtitlesoup))
# 제목 정보를 리스트에 취합 , 취합하면서 앞뒤 공백 모두 제거 상태로 취합
# for item in newtitlesoup:
#     print(item.find_all('a')[0].text)  # .text ==> 해당 태그 정보에서 text 속성만 반환해줘
#
youtubetitlelist = [  item.find_all('a')[0].text.strip()  for item in newtitlesoup ]
print(youtubetitlelist)
#리스트 내포 와 정규표현식 를 이용해서 위 youtubetitlelist 항목을
# 한줄로 영문대소문자만 남기도록 수정
# youtubetitlelist = [ re.sub(r'[^a-zA-Z\s]+','',item)  for item in youtubetitlelist ]
# print(youtubetitlelist)
#
#stringdata = '\n'.join(youtubetitlelist)
#print(stringdata)
import re
# 정규 표현식을 활용해서 전체 문자열 중에 영문대소문자와 공백을 제외한 모든 텍스트 삭제
print("="*80)
# result = re.findall(r'[a-zA-Z\s]+', stringdata)
# print(''.join(result))
# result = re.sub(r'[^a-zA-Z\s]+','',stringdata)
# print(result)
import pandas as pd
mydf = pd.DataFrame(youtubetitlelist,columns=['제목'])
print(mydf)
mydf.to_excel("youtubedata.xlsx", index=False)

# newtitlesoup = soup.find_all('td', class_ = 'subscriber_cnt')  # 리스트로  반환
# print(len(newtitlesoup))
# for item in newtitlesoup:
#     print(item.text)  # .text ==> 해당 태그 정보에서 text 속성만 반환해줘


