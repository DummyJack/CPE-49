# 題目網址: https://onlinejudge.org/external/113/11332.pdf
# Summing Digits

def cal(n): # 計算g(n)，得到僅有一位數字的值
    count = 0
    while n > 0:
        count += n % 10
        n //= 10
    return count

while True:
    n = int(input())
    
    if n == 0: # 0 結束
        break
    
    while n >= 10: #  n >= 10，繼續計算
        n = cal(n)
    
    print(n)
    
# ex.
# n = 11
# f(n) = 1+1 = 2