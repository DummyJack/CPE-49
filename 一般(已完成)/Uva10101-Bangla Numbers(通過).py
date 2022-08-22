# 題目網址: https://onlinejudge.org/external/101/10101.pdf
# Bangla Numbers

def f(n): # 定義題目，錢幣換算
    if n >= 10000000:
        f(n // 10000000)
        print(' kuti', end = '')
        n %= 10000000

    if n >= 100000:
        f(n // 100000)
        print(' lakh', end = '')
        n %= 100000
        
    if n >= 1000:
        f(n //1000)
        print(' hajar', end = '')
        n %= 1000
        
    if n >= 100:
        f(n // 100)
        print(' shata', end = '')
        n %= 100
        
    if n >= 1:
        print(f" {n}", end = '')
        
t = 1
while True:
    a = int(input())
    print('%5s' %(f'{t}.'), end='')
    if a > 0:
        f(a)
    else:
        print(' 0', end = '')
    print(end = '\n')
    
    t += 1
    