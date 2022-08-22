# 題目網址: https://onlinejudge.org/external/102/10242.pdf
# Fourth Point!!

while True:
    
    points = list(map(float, input().split())) # 測試資料
    
    p_a = points[0], points[1] # 第一個邊的端點(x, y)座標
    p_b = points[2], points[3] # 第一個邊的另一端點(x, y)座標
    p_x = points[4], points[5] # 第二個邊的端點(x, y)座標
    p_y = points[6], points[7] # 第二個邊的另一端點(x, y)座標
    
    if p_x == p_b:
        p_c = p_y
    elif p_y == p_b:
        p_c = p_x
    elif p_x == p_a:
        p_c = p_y
        p_a, p_b = p_b, p_a
    else:
        p_c = p_x
        p_a, p_b = p_b, p_a

    p_d = p_c[0] + (p_a[0] - p_b[0]), p_a[1] + (p_c[1] - p_b[1]) # 第四個點的(x, y)座標
    
    print('%.3f %.3f' %(p_d[0], p_d[1])) # 只取到小數點後三位

# 平行四邊形ABCD公式，A+C = B+D