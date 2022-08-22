# 題目網址: https://onlinejudge.org/external/100/10071.pdf
# Back to High School Physics

while True:
    
    n = list(map(int, input().split()))
    for i in range(0, len(n), 2):
        v = n[i] # 速度
        t = n[i+1] # 時間
        
        s = 2 * v * t # 位移
        
        print(s)

# 解題想法: 求位移

# 位移如何求
# v = a*t，a = v/t
# s = (1/2)*a*t²
# a 代入 s， s = (1/2)*(v/t)*t² = (1/2)*v*t
# t = 2t 代入 s， s = 2 * v * t
