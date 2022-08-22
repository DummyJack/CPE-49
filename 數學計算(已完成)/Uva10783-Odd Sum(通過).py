# 題目網址: https://onlinejudge.org/external/107/10783.pdf
# Odd Sum

t = int(input()) # 測資

for i in range(t):
    
    a = int(input())
    b = int(input())
    
    count = 0
    if a % 2 != 0: # 假如 a 是奇數
        for j in range(a, b+1, 2):
            count += j
    else:
        for j in range(a+1, b+1, 2):
            count += j
    
    print(f'Case {i + 1}: {count}')
        
    
# 給一個範圍 a 到 b (輸入)
# 找出 a 和 b 之間所有奇數的和 (輸出)