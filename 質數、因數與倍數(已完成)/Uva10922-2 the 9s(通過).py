# 題目網址: https://onlinejudge.org/external/109/10922.pdf
# 2 the 9s

from sys import stdin

def sum_digits(num):
  total = 0
  while num > 0:
    num, r = divmod(num, 10)
    total += r
  return total


while True:
  n = stdin.readline().strip()

  if n == "0":
    break
  
  if n == "9":
    count = 1
    flag = True
  else:
    count = 1
    num = sum(map(int, list(n)))
    if num % 9 == 0:
      flag = True
      while num > 9:
        num = sum_digits(num)
        count += 1
    else:
      flag = False

  if flag:
    print(f"{n} is a multiple of 9 and has 9-degree {count}.")
  else:
    print(f"{n} is not a multiple of 9.")