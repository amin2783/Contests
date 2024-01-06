from math import sqrt

d = dict()

def factorize(n):
    if n in d:
        
        factors = d[n]
        factors.append(n)
    factors = [1, n]
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            factors.append(n//i)
    d[n] = sorted(factors)










for tc in range(int(input())):
    a, b = map(int, input().split())

    # if b%a == 0:
    # x = 2*b
    # k = 2

    # while x%a!=0 or x%b!=0:
    #     k+=1
    #     x = k*b
    
    # else:
    x = a*b
    k = x//b

    while x%a!=0 or x%b!=0:
        k+=1
        x = b*k
        # x = x + (k*b)
    
    print(x)