# 題目網址: https://onlinejudge.org/external/108/10812.pdf
# Beat the Spread!

t = int(input()) # 測資

for i in range(t):
    
    n = list(map(int, input().split()))
    for j in range(0, len(n), 2):
        
        s = n[j] # 分數總合(>0)
        d = n[j+1] # 分數差的絕對值(>0)
        
        a = s + d
        b = s - d
        
        if a < 0 or b < 0 or a % 2 != 0 or b % 2 != 0:
            print('impossible')
        else:
            print('%d %d' %(a / 2, b / 2))
            
# 設兩隊得分為 a b

# 聯立
# a + b = s  -->  2a = s + d
# a - b = d       2b = s - d

# a = s+d/2, b = s-d/2