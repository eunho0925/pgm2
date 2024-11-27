import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp

x = ['a', 'b', 'c']
y = [3, 4, 8]
plt.plot(x, y)

print(plt.plot(x, y))

plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.title('Line Graph')

plt.plot(x, y)
plt.title('꺾은선 그래프')

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결


import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용 가능한 폰트 확인
font_list = [f.name for f in fm.fontManager.ttflist]
font_list.sort()  # 리스트를 오름차순으로 정렬
# 한 줄에 한 항목씩 출력
print('\n'.join(map(str, font_list)))

plt.plot(x, y)
plt.title('꺾은선 그래프')
plt.show()

plt.plot([-1, 0, 1], [-5, -1, 2])