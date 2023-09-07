from math import ceil

for tc in range(int(input())):
    a, b, c = map(int, input().split())

    print(ceil((abs(a-b))/(c*2)))