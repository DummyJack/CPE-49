# 題目網址: https://onlinejudge.org/external/100/10019.pdf
# Funny Encryption Method

a = list(input().split())

if len(a) == 1: # 假如一開始輸入只有一個數字
    
    t = int(''.join(a)) # 測資
    for i in range(t): 
        
        n = input()
        
        x1 = int(n) # 十進位
        x2 = int(n, 16) # 十進位轉成十六進位
        
        x1 = bin(x1) # 十進位轉成二進位
        x2 = bin(x2) # 十六進位轉成二進位
        
        b1 = len([x for x in x1 if x == '1']) # 計算 x1 出現幾次 1
        b2 = len([x for x in x2 if x == '1']) # 計算 x2 出現幾次 1
    
        print(f'{b1} {b2}')

else:
    for i in range(int(a[0])): # a[0] 測資
        
        n = a[i+1] # 測資後面的數字(計算)

        x1 = int(n)
        x2 = int(n, 16)
        
        x1 = bin(x1)
        x2 = bin(x2)
        
        b1 = len([x for x in x1 if x == '1'])   
        b2 = len([x for x in x2 if x == '1'])  
        
        print(f'{b1} {b2}')