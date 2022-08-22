# 題目網址: https://onlinejudge.org/external/114/11417.pdf
# GCD

import math

def f(n):
    g = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            g += math.gcd(i, j)
    return g

while True:
    
    n = int(input())
    
    if n == 0:
        break
    
    print(f(n))