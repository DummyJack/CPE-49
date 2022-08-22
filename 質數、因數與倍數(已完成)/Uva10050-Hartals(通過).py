# 題目網址: https://onlinejudge.org/external/100/10050.pdf
# Hartals

t = int(input()) # 測資

for k in range(t):
    
    n = int(input()) # 模擬天數
    p = int(input()) # 幾個政黨
    c = [0] * p
    
    for i in range(p):
        c[i] = int(input()) # 政黨罷會的參數
    
    # 模擬罷會
    total = 0
    for i in range(1, n+1):
        if i % 7 == 6 or i % 7 == 0: # 跳過星期五、星期六
            continue
        
        # 只要罷會，+1
        for j in range(p):
            if i % c[j] == 0:
                total += 1
                break
            
    print(total) # 損失多少的工作天