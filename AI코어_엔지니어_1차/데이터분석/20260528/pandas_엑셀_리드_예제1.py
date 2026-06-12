import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns  # 시각화 패키지(라이브러리)
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)


youdf = pd.read_excel("youtube_data.xlsx", index_col=0) # 엑셀파일 읽어서 DataFrame 객체로 생성
#print(youdf)
#youdf.info()
print( youdf.head(30) )

# Video 컬럼 데이터 기준으로 Top 10 항목을 추출해서 출력
# 1차 ==> Video 컬럼 데이터를 수치 데이터 모두 일관 변환
def VideoDataControl(arg):
    return re.sub(r'[,개]','',arg)

youdf['Video'] = youdf['Video'].apply(VideoDataControl)
print(youdf.head(10))
youdf.info()
youdf['Video'] = youdf['Video'].astype('int64')  # 특정컬럼데이터를 일괄 타입변환해주는 메서드
youdf.info()

# 2차 ==> Video 컬럼 데이터 기준으로 내림차순 정렬(sort_values)
# ascending=False : 내림차순
# ascending=True : 오름차순
youdf.sort_values(by='Video', inplace=True, ascending=False)
#print(youdf.head(30))
# 3차 ==> head(10).copy()
youdf_top10 = youdf.head(10).copy()
print(youdf_top10)
sns.barplot(data=youdf_top10, x='ChannelName', y='Video', palette="Set3")
plt.show()
# # ChannelName 컬럼을 인덱스로 설정해주고
# # Video 컬럼만 남게 Dataframe 을 수정해주세요
# youdf_top10 = youdf_top10[['ChannelName','Video']]
#
# youdf_top10.set_index('ChannelName', inplace=True)
# print(youdf_top10)
# # 그 수정된 Dataframe을 막대차트로 시각화 시켜주세요
# youdf_top10.plot.bar()
# #plt.savefig("chart1.JPEG")
# plt.show()