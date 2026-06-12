import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화


# fig = plt.figure( figsize=(12,6) )
#
# ax1 = fig.add_subplot(1,2, 1)
# ax2 = fig.add_subplot(1,2, 2)
#
# ax1.bar([10,20,30,40,50],[20,60,80,90,120])
# ax2.plot([10,20,30,40,50],[20,60,80,90,120])  # 차트 랜더링 --> 디폴트 선그래프
# plt.show() # 화면에 출력
# # plt.savefig('linechart.jpeg') # 현재 차트를 이미지 파일로 저장

fig, axes = plt.subplots(1,2, figsize=(12,6))

axes[0].bar([10,20,30,40,50],[20,60,80,90,120])
axes[1].plot([10,20,30,40,50],[20,60,80,90,120])

plt.show()