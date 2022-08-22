# 題目網址: https://onlinejudge.org/external/102/10226.pdf
# Hardwood Species

from collections import Counter
from sys import stdin, stdout

def print_trees(tress):
    for k, v in sorted(trees.items()): 
        message = '{} {:.4f}\n'.format(k, v/total*100) # k: 樹種的名稱 v: 所佔的比例(到小數點後4位)
        stdout.write(message)


try:
    t = int(stdin.readline()) # 測資
    stdin.readline() # 樹木的名稱

    for i in range(t):
        trees = Counter()
        total = 0
        while True:
            line = stdin.readline().strip()
            if line == '':
                print_trees(trees)
                if i < t-1: # 測試資料間空一列
                    print()
                break
            
            trees[line] += 1
            total += 1
except:
    pass
            