from math import sqrt

for tc in range(int(input())):
    n = int(input())
    ai = sum(map(int, input().split()))

    # summ = sum(ai)

    if int(sqrt(ai))**2 is ai:
        print("YES")
    else:
        print("NO")