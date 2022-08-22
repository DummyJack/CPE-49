# 題目網址: https://onlinejudge.org/external/101/10193.pdf
# All You Need Is Love!

n = int(input())

for k in range(n):
    
    s1 = list(input())
    s2 = list(input())
    
    a, b = 0, 0
    
    t = 0
    for i in range(len(s1)-1, -1, -1):
        if s1[i] == '1':
            a += 2**t
        t += 1
        
    t = 0
    for i in range(len(s2)-1, -1, -1):
        if s2[i] == '1':
            b += 2**t
        t += 1
    
    while b > 0:
        a, b = b, a%b
        
    if a != 1:
        print(f'Pair #{k+1}: All you need is love!')
    else:
        print(f'Pair #{k+1}: Love is not all you need!')
        
