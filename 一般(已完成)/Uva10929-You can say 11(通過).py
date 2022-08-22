
# 題目網址: https://onlinejudge.org/external/109/10929.pdf
# You can say 11

while True:
    n = int(input())
    if n == 0:
        break
    
    if n % 11 == 0:
        print('%d is a multiple of 11.' %(n))
    else:
        print('%d is not a multiple of 11.' %(n))
        
# 判斷輸入的數字是不是 11 倍數