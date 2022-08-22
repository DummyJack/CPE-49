# 題目網址: https://onlinejudge.org/external/120/12019.pdf
# Doom’s Day Algorithm

from time import strftime
from datetime import datetime

year = 2011
t = int(input()) # 測資
for i in range(t):
    m, d = map(int, input().split())
    weekday = datetime(year, m, d).strftime('%A') # %A 本地完整星期名稱
    print(weekday)
        
# 解題想法
# 2011年，幾月幾號(input)是星期幾(output)