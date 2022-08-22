# 題目網址: https://onlinejudge.org/external/2/272.pdf
# TeX Quotes

c = 0
while True:
    try:
        n = input()
    except:
        break
    
    a = []
    for i in n:
        if i == "\"": # "為特殊符號，所以必須加反斜線(\)
            # 內部/外部 交替變換
            if c == 0:
                # 在內部遇到雙引號，輸出``
                a.append("``")
                c = 1
            else:
                # 在內部遇到雙引號，輸出''
                a.append("''")
                c = 0
        else:
            a.append(i)
        
    print("".join(a))