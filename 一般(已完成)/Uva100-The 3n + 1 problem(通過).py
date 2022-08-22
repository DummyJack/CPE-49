# 題目網址: https://onlinejudge.org/external/1/100.pdf
# The 3n + 1 problem

def cal_circle(number):
    count = 1
    while number != 1: # n = 1，stop
        if number % 2 != 0:
            number = number * 3 + 1
        else:
            number = number / 2
        count += 1 
    return count # circle length

# print(cal_circle(22))
# 輸入22，得到的數列: 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1，總共16個數字(cycle length)
while True:
    a = list(map(int, input().split()))
    for i in range(0,len(a),2):
        n = a[i]
        m = a[i+1]
        if n < m:
            max_value = 1
            for i in range(n , m+1):
                x = cal_circle(i)
                if max_value < x: # 找出最長的 cycle length
                    max_value = x 
        else: 
            max_value = 1
            for i in range(m , n+1):
                x = cal_circle(i)
                if max_value < x:
                    max_value = x 
                    
        print("%d %d %d" %(n, m, max_value))
