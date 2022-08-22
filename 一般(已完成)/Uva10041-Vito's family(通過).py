# 題目網址: https://onlinejudge.org/external/100/10041.pdf
# Vito’s family

n = int(input()) # 測資
for k in range(n):
    temp = input().split() 
    r = temp[0] # 親戚的數目
    temp.remove(r)
    r = int(r) 
    
    for i in range(0, r):
        temp[i] = int(temp[i]) # 親戚房子的門牌號碼
    temp.sort()
    mid = temp[r // 2] 
    ans = 0
    for i in temp:
        ans += abs(i - mid) # 絕對值
    print(ans)
    
# 解題想法
# 找到輸入數字的中位數，接下來，計算每一個點到中位數的距離，最後加總起來。