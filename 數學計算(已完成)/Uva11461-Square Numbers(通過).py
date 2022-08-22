# 題目網址: https://onlinejudge.org/external/114/11461.pdf
# Square Numbers

import math

# 判斷完全平方，是(True)，不是(False)
def is_sqr(n):
    m = int(math.sqrt(n))
    return m * m == n

flag = True
while flag:
    p = list(map(int, input().split()))
    
    # 如果超過一組的話就把0 0弄掉，然後用for執行完這輪後停止
    # 如果只有1組的話就用 while True把每一組執行完

    if len(p) > 2: # 如果這組超過2個，就把0 0去掉(不然會被放進for裡面處理)
        p = p[:-2]
        flag = False # 視為最後一組輸入
        
    if p[0] == 0 and p[1] == 0: # 如果這組只有2個且是 0 0 就結束程式
        break
    
    for k in range(0, len(p), 2): 
        
        a = p[k]
        b = p[k+1]
            
        count = 0
        for i in range(a, b+1):
            if is_sqr(i) == True: # 如果是完全平方，count + 1
                count += 1
        print(count) # 輸出