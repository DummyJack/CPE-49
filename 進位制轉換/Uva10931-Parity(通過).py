# 題目網址: https://onlinejudge.org/external/109/10931.pdf
# Parity

while True:
    n = list(map(int, input().split()))
    for k in range(0, len(n)):
        i= n[k]
        
        if i == 0: # 0 結束
            break
        
        b = '{0:b}'.format(i) # 十進位轉二進位
        p = b.count('1') # b 中的 1 出現幾次

        print(f'The parity of {b} is {p} (mod 2).')
        