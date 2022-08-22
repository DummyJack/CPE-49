# 題目網址: https://onlinejudge.org/external/100/10035.pdf
# Primary Arithmetic

flag = True
while flag:
    n = list(map(int, input().split()))
    
    # 如果超過一組的話就把0 0弄掉，然後用for執行完這輪後停止
    # 如果只有1組的話就用 while True把每一組執行完

    if len(n) > 2: # 如果這組超過2個，就把0 0去掉(不然會被放進for裡面處理)
        n = n[:-2]
        flag = False # 視為最後一組輸入
        
    if n[0] == 0 and n[1] == 0: # 如果這組只有2個且是 0 0 就結束程式
        break
        
    for i in range(0,len(n),2):
        n1 = n[i]
        n2 = n[i+1]  
        
        count = 0
        c = 0
        for i in range(10):
            
            c = n1%10 + n2%10 + c
            if c > 9:
                c = 1
            else:
                c = 0
            count += c
            
            n1 //= 10 # 將個位數字捨棄掉
            n2 //= 10  
            
            
        if count == 0:
            print('No carry operation.')
        elif count == 1:
            print('1 carry operation.')
        
        else:
            print('%d carry operations.' %count)
        