# 題目網址: https://onlinejudge.org/external/104/10420.pdf
# List of Conquests

a = {}

n = int(input()) # 人數

for i in range(n):
    c = list(input().split()) # 國籍和名字
    
    if c[0] not in a:
        a[c[0]] = 1
    else:
        a[c[0]] += 1
        
b = sorted(a) # 按照國籍的英文字母排序
for i in b:
	print("{} {}".format(i, a[i])) # 輸出國籍與該國人數
