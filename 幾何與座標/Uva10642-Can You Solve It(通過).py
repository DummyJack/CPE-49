# 題目網址: https://onlinejudge.org/external/106/10642.pdf
# Can You Solve It?

a = list(map(int, input().split()))

if len(a) == 1:
    for i in range(a[0]): # 測資
        
        points = list(map(int, input().split()))
        
        # (x1, y1) --> (x2, y2)
        y1 = points[0]
        x1 = points[1]
        y2 = points[2]
        x2 = points[3]
        
        # 每個點對應的路徑上的位置: （x+y）*（x+y+1）/ 2 + y
        n = int((x1 + y1) * (x1 + y1 + 1) / 2 + y1)
        m = int((x2 + y2) * (x2 + y2 + 1) / 2 + y2) 
            
        print(f'Case {i+1}: {m-n}') # m-n，代表兩點經過多少點可以到達
else:
    for i in range(a[0]): # 測資
        
        points = a[1:]
        
        y1 = points[0]
        x1 = points[1]
        y2 = points[2]
        x2 = points[3]
        
        n = int((x1 + y1) * (x1 + y1 + 1) / 2 + y1)
        m = int((x2 + y2) * (x2 + y2 + 1) / 2 + y2) 
            
        print(f'Case {i+1}: {m-n}')