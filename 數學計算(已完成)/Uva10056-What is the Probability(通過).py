# 題目網址: https://onlinejudge.org/external/100/10056.pdf
# What is the Probability

t = int(input()) # 測資

for k in range(t):
    
    n, p, i = map(float, input().split()) # n:玩家數、p:成功機率、i:第幾個玩家
    
    q = 1- p
    a = pow(q, i-1) * p
    r = pow(q, n)
    
    if p == 0:
        print('0.0000')
    else:
        print('%.4f' %(a * (1 - pow(r, 100)) / (1-r))) 
        
# 輸出 i-th 玩家成功的機率