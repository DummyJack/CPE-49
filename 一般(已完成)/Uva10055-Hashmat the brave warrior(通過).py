# 題目網址: https://onlinejudge.org/external/100/10055.pdf
# Hashmat the brave warrior

while True:
    n = list(map(int, input().split()))
    
    for i in range(0,len(n),2):
        
        a = n[i] # Hashmat
        b = n[i+1] # 敵人的士兵數

        # 輸出 Hashmat 與敵人士兵數目的差
        print(abs(a - b)) 
            
