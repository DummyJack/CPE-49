# 題目網址: https://onlinejudge.org/external/100/10038.pdf
# Jolly Jumpers

while True:
    try:
        a = list(map(int, input().split())) # 第一個數字為測資數量
    except: # 最後要輸入Ctrl+Z，終止輸入
        break
    
    n = [0] * len(a)
    
    # 這樣判斷可以在發現不是 Jolly 的當下就結束判斷
    for i in range(2, len(a)):
        try:
            m = abs(a[i] - a[i-1])
            if n[m] == 1 or m == 0: # 如果這個差的值出現過了，或差 = 0，就不是
                print('Not jolly')
                break
            else:
                n[m] = 1
        except: # 如果這個差的值太大，就不是
            print('Not jolly')
            break
    else: # 如果沒有被 break 
        print('Jolly')