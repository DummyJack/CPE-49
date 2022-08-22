# 題目網址: https://onlinejudge.org/external/101/10190.pdf
# Divide, But Not Quite Conquer!

while True:
    n, m = map(int, input().split())

    arr = [n]

    s = 0 # s作為輸出的機關
    w = 0

    if(n < m or m <= 1 or n <= 1):
        print('Boring!')
        w += 1
    if(w == 0):
        while(n%m == 0):
            arr.append(n // m)
            if(n // m == 1):
                break
            n = n // m
        if(n%m != 0):
            s += 1
            print('Boring!')
        if(s==0):
            print(*arr)
            
# 解題想法
# 解是不是次方