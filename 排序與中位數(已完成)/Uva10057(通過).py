# 題目網址: https://onlinejudge.org/external/100/10057.pdf
# A mid-summer night’s dream

while True:

    n = int(input()) # 測資
    list1 = [] 
    
    for i in range(n):
        list1.append(int(input()))
    
    list1.sort()
    x = list1[(n-1) // 2] # 中位數
    y = list1[n // 2]
    
    count = 0
    for i in range(n):
        if list1[i] == x or list1[i] == y: # 中位數總數
            count += 1 
    
    d = y-x+1 # 滿足中位數條件數
    print(x, count, d)
    
# 第一筆資料 2 10 10
# 中位數 (10+10) / 2 = 10
# 中位數總數: 10 10 --> 2
# 中位數條件: 10-10+1 = 1

# 如果數字總數為奇數，符合中位數條件必為一。