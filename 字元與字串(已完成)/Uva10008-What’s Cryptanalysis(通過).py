# 題目網址: https://onlinejudge.org/external/100/10008.pdf
# What’s Cryptanalysis?

a = {chr(65+i): 0 for i in range(26)} # chr('A') = 65, chr('Z') = 90
n = int(input()) # 測資數量

for i in range(n):
    m = list(input().split())
    for j in m:
        for k in range(0, len(j)): # 一個一個的字母拿出來
            x = ord(j[k])
            if x >= 65 and x <= 90:
                a[chr(x)] += 1
            elif x >= 97 and x <= 122: # chr('a') = 97, chr('z') = 122
                a[chr(x-97+65)] += 1 # 把小寫的字母變成大寫計算

b = sorted(a.items(), key = lambda d:d[1], reverse=True) # 以字母出現的次數進行排列，由大到小
for key, value in b:
    if value > 0: # 沒出現的字母不需要輸出
        print('{} {}'.format(key, value))