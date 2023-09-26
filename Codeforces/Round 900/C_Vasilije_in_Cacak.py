from math import sqrt, floor
from itertools import combinations


def is_possible_sum(n, k, s):  
    numbers = [i for i in range(1,n+1)]

    b = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        b[i][0] = True
    for i in range(1, s + 1):
        b[0][i] = False
    for i in range(k, k+1):
        for j in range(1, s + 1):
            if j < numbers[i - 1]:
                b[i][j] = b[i - 1][j]
            if j >= numbers[i - 1]:
                b[i][j] = (b[i - 1][j] or b[i - 1][j - numbers[i - 1]])
    return b[n][s]




for tc in range(int(input())):
    n, k, x = map(int, input().split())

    while True:
        if (x < ((k*(k+1))/2)) and (x > ((n*(n+1))/2)):
            print("NO")
            break
        if is_possible_sum(n,k,x):
            print("YES")
            break
        else:
            print("NO")
            break
    