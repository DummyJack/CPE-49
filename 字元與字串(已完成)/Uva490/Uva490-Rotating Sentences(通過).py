# 題目網址: https://onlinejudge.org/external/4/490.pdf
# Rotating Sentences

def func1(x):
    for i in range(len(x)-1, -1, -1): # 從前往後刪
        if x[i] is None:
            del x[i] # 把 None 的地方刪掉
        else:
            break
        
    for i in range(len(x)):
        if x[i] is None: # 紅色的部分
            x[i] = ' '
    return x

lines = []
max_length = 0

while True:
    try:
        input1 = input()
        if len(input1) > max_length: # 找出最長的輸入字串(第二行)
            max_length = len(input1) 
        lines.append(input1) 

    except: # 最後要輸入Ctrl+Z，終止輸入
        break

out_lines = [[None for i in range(len(lines))] for j in range(max_length)] # 空格的地方(黃色)填 None
lines = lines[::-1] # 順序相反操作，例:[3, 2, 1] --> [1, 2, 3]

for index1, i in enumerate(lines): # 絕對位置
    for index2, j in enumerate(i):
        out_lines[index2][index1] = j

for i in out_lines:
    print(''.join(func1(i)))
