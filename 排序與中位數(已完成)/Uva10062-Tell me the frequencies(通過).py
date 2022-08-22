# 題目網址: https://onlinejudge.org/external/100/10062.pdf
# Tell me the frequencies!

c = 0
while True:
    
    s = input()
    
    a = [0 for i in range(257)] # ASCII 碼表總共有 256 字元
    
    for i in s: # ASCII值出現的次數
        a[ord(i)] += 1
    
    if c > 0: # 測試資料間空一列
        print()
    c += 1
    
    for i in range(1, len(s)+1): # 次數由小到大輸出
        for j in range(256, 0, -1):
            if a[j] == i: # 如果有2個以上的字元有相同的次數，則ASCII值較大的先輸出
                print(j, i) 
        