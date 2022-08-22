# 題目網址: https://onlinejudge.org/external/104/10415.pdf
# Eb Alto Saxophone Player

# 薩克斯風指法
# 八個音名，十根手指
# 大寫代表高八度
a = {'c':[2, 3, 4, 7, 8, 9, 10], 'd':[2, 3, 4, 7, 8, 9], 
    'e':[2, 3, 4, 7, 8], 		 'f':[2, 3, 4, 7],
	'g':[2, 3, 4], 			 'a':[2, 3], 
	'b':[2], 					 'C':[3], 
	'D':[1, 2, 3, 4, 7, 8, 9],  'E':[1, 2, 3, 4, 7, 8],
	'F':[1, 2, 3, 4, 7], 		 'G':[1, 2, 3, 4],
	'A':[1, 2, 3], 			 'B':[1, 2]}

t = int(input()) # 測資

for i in range(t):
    
    m = input() # 每筆測資輸入歌曲的一連串音名，有可能為空
    
    sum = [0 for i in range(11)] # sum 紀錄十個按鍵是否被按著(0: 沒按, 1: 有按)
    now = [0 for i in range(11)] # now 紀錄十個按鍵是否被按著
    
    for i in m:
        for j in range(1, 11):
            if j in a[i]:
                if now[j] != 1: # 原先沒按下，這次有按的，案件次數 +1
                    sum[j] += 1
                    now[j] = 1
            else: # 如果這次沒有被按下的鍵，改為0(沒按)
                now[j] = 0 
                
    for i in range(1, len(sum)): 
        if i > 1: # 輸出的數字用空格分隔
            print(' ', end = '') 
        print(sum[i], end = '') # 每個手指的按下次數
    print() # 輸入一行。輸出一行