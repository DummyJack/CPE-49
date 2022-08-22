# 題目網址: https://onlinejudge.org/external/2/299.pdf
# Train Swapping

n = int(input()) # 測資數量
for k in range(n):
    l = int(input()) # 火車的長度
    a = list(map(int, input().split())) # 火車車廂的當前順序
    count = 0
    for i in range(l): # 反轉表
        for j in range(i):  
            if a[j] > a[i]:
                count += 1
    print("Optimal train swapping takes %d swaps." %(count))
    
# 補充
# 反轉表(Inversion table)
#       紀https://onlinejudge.org/external/2/299.pdf錄每個車廂的左側有多少個車廂編號大於該車廂
#       左邊車廂編號有幾項比較大，代表需要調換的次數
# 例:
# 原始資料: 4 1 3 2
# 反轉表: 
#       車廂編號  1 2 3 4
#                1 2 1 0
# 調換次數: 1+2+1+0=4 