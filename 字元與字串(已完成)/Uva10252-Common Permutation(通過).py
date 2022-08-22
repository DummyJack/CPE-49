# 題目網址: https://onlinejudge.org/external/102/10252.pdf
# Common Permutation

from collections import Counter

def common_permutation(a, b):
    print(''.join(k * v for k, v in sorted((Counter(a) & Counter(b)).items())))

while True:
    try:
        a = input().strip()
        b = input().strip()
        common_permutation(a, b)
    except:
        break