# 題目網址: https://onlinejudge.org/external/102/10268.pdf
# 498-bis

while True:

    x = int(input()) # x的值
    a = list(map(int, input().split())) # 多項式各項係數
    
    ans = 0
    n = len(a) - 1
    
    for i in range(n):
        ans += a[i] * (n-i) * pow(x, n-1-i)
    print(ans)

    
# ex

# input: 7 (x = 7)
# input: 1 - 1 (x-1)
# x-1 微分 --> 1，不用代入x
# output: 1

# input: 2 (x = 2)
# input: 1 1 1 (x^2 + x + 1)
# x^2 + x + 1 微分 -- > 2x + 1，代入 x = 2
# output: 5