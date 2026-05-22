import requests # 특정 url의 웹페이지(html)정보를 요청하는 패키지
from bs4 import BeautifulSoup   # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# bs4 패키지 안에서 BeautifulSoup 클래스만 가져와~
import re


url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube' # html 정보 요청할 url
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers, timeout=10)  # 웹페이지 요청
html = r.text  # r.content (바이트로 가져옴  Or r.text (문자열로 가져옴)
# print(html)

soup = BeautifulSoup(html, 'lxml')  # 파서 지정
#html.parser보다 lxml은 파싱할 때의 속도가 빠름!
# but, 이건 내장된 게 아니라 pip install로 깔아야 함

# 위 방법과 다른 find_all(), find() 메서드 활용
# newtitlesoup = soup.find_all(class_ = 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1')
# #soup.find_all은 태그 정보를 찾아주는 메소드
#
# print(newtitlesoup[0].text) # .text는 그 태그정보 중에서 text만 반환해달라는 메소드
# print(newtitlesoup[5].text)
#
# for i in range(len(newtitlesoup)):
#     print(newtitlesoup[i].text)

newtitlesoup = soup.find_all(class_ = 'subject')
#soup.find_all은 태그 정보를 찾아주는 메소드

print(len(newtitlesoup))


print(newtitlesoup[0].text) # .text는 그 태그정보 중에서 text만 반환해달라는 메소드
text_list = []

for i in range(len(newtitlesoup)):
    text = newtitlesoup[i].get_text(separator='\n', strip=True)
    text_list.append(text)
    result = ' '.join(text_list)
print(result)

try:
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
except requests.exceptions.ConnectionError:
    print("서버가 연결을 끊었습니다. headers나 URL을 확인하세요.")
except requests.exceptions.Timeout:
    print("요청 시간이 초과되었습니다.")
except requests.exceptions.HTTPError as e:
    print("HTTP 오류:", e)

    print(newtitlesoup[i].text)
#soup.find_all은 태그 정보를 찾아주는 메소드

newtitlesoup = soup.find_all(class_ = 'subscriber_cnt') #리스트로 반환
for item in newtitlesoup[1:]:
    print(item.text)
