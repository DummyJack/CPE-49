# 題目網址: https://onlinejudge.org/external/110/11063.pdf
# B2-Sequence

case = 1
while True:
    try:
        input1 = list(map(int, input().split()))
        
        if len(input1) == 0: # 輸入是空格
            continue
        
        if len(input1) == 1: # 輸入一個數字
            input1 = list(map(int, input().split()))
            list1 = [input1]
        else: # 輸入多個數字
            list1 = []
            index = 0
            while index < len(input1): # 分辨輸入幾筆測資，把一個一個分開，例:3 1 2 3 2 3 4 -- > [3,1,2,3] and [2,3,4]
                num = input1[index]
                list1.append(input1[index+1:index+num+1])
                index += num+1
    except:
        break
    
    for i in list1:
        set1 = set()
        flag = True
        for j in range(len(i)):
            for k in range(j+1):
                    if (i[j] + i[k]) in set1: # ij + ik （j <= k）皆不相等
                        flag = False
                        break
                    else:
                        set1.add(i[j] + i[k])
                
        if flag:
            print(f'Case #{case}: It is a B2-Sequence.\n')
        else:
            print(f'Case #{case}: It is not a B2-Sequence.\n')
        case += 1  
