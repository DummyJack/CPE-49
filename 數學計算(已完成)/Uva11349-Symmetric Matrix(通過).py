# 題目網址: https://onlinejudge.org/external/113/11349.pdf
# Symmetric Matrix

t = int(input()) # 測資

for k in range(t):
    
    N = input().split()
    n = int(N[2]) # 矩陣的維度
    arr = []
    
    # 矩陣內的元素數值
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    # 判斷是否為對稱矩陣
    is_Symmetric = True
    center = n // 2
    for i in range(n):
        for j in range(i+1):
            if arr[i][j] < 0 or  arr[n-1-i][n-1-j] < 0:
                is_Symmetric = False
                break
            if arr[i][j] != arr[n-1-i][n-1-j]:
                is_Symmetric = False
                break
            
    # 輸出
    if is_Symmetric:
        print(f'Test #{k+1}: Symmetric.')
    else:
        print(f'Test #{k+1}: Non-symmetric.')
        