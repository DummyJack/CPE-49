# 題目網址: https://onlinejudge.org/external/102/10235.pdf
# Simply Emirp

def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True

while True:
    n = input()
    rn = n[::-1]
    
    rn = int(rn)
    n = int(n)
    
    if prime(n) == False:
        print(f'{n} is not prime.')
        
    elif prime(n) == True and prime(rn) == True and n != rn:
        print(f'{n} is emirp.')
        
    else:
        print(f'{n} is prime.')
        
    