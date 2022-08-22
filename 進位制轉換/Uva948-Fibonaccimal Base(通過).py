# 題目網址: https://onlinejudge.org/external/9/948.pdf
# Fibonaccimal Base (費氏進位表示法)

fibs = list(range(40))
# 最開頭兩項的初值
fibs[0] = 0
fibs[1] = 1

for i in range(2, 40): # 計算到f[39]
    fibs[i] = fibs[i-1] + fibs[i-2] # 用前兩項相加計算下一項

a = list(map(int, input().split()))

if len(a) == 1:
    for x in range(a[0]): # a[0] = 測資
        d = int(input()) # DEC_BASE(原始的十進位數字)
        print(str(d) + ' = ', end='')
        
        isPut = False
        for i in range(39,1,-1):
            if d >= fibs[i]:
                d = d - fibs[i]
                isPut = True
                print('1', end='')
            elif isPut == True:
                print('0', end='')
        print(' (fib)')
        
else:
    for x in range(a[0]): 
        d = a[x+1] 
        print(str(d) + ' = ', end='')
        
        isPut = False
        for i in range(39,1,-1):
            if d >= fibs[i]:
                d = d - fibs[i]
                isPut = True
                print('1', end='')
            elif isPut == True:
                print('0', end='')
        print(' (fib)')
        
# 費式數列
# 第 i 項	0	1	2	3	4	5	6	7	8	9
# Fib(i)	0	1	1	2	3	5	8	13	21	34

# 0 來表示沒有用到的項，以 1 來表示有用到的項，由右至左排列。
# 例: 17 = 100101 (fib)
# 17     =	1	0	0	1	0	1
# 13+3+1 =	13	8	5	3	2	1