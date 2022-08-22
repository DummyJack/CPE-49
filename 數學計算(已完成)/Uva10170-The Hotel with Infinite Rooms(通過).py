# 題目網址: https://onlinejudge.org/external/101/10170.pdf
# The Hotel with Infinite Rooms

from sys import stdin
import math

for f in stdin:
    
    S,D = map(int, f.split())
    f = (2 * D)+(S * S) - S
    ans = ((-1 + ((1-4*(-f)) ** 0.5)) / 2)
    print(math.ceil(ans))
    
'''    S+(S+1)+(S+2)+……+n=((S+n)×(n–S+1))/2 (等差級數梯形公式) ≤ D 
                (n 為最小符合此式的整數值)                      '''