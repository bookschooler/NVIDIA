import pandas as pd
import re

newsdf = pd.read_excel("navernews.xlsx")
#print(newsdf)
#print(newsdf['뉴스 제목'][0])
# for item in newsdf['뉴스 제목']:
#     print( re.sub(r'[^가-힣\s]+','',item) )
#     print('='*50)

print( newsdf )
print("="*80)

def newstitlefiltering(arg):
    #print('arg : ', arg)
    #print( re.sub(r'[^가-힣\s]+', '', arg) )
    return re.sub(r'[^가-힣\s]+', '', arg)

newsdf['뉴스 제목'] = newsdf['뉴스 제목'].apply(newstitlefiltering)
print(newsdf)
newsdf.to_excel("navernews_filtering.xlsx", index=False)