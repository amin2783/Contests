from math import ceil

for tc in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) <= k:
        print(n)
    else:
        first_hit = ceil(k/2)
        last_hit = k//2

        first_total = a[0]

        i = 0
        while first_total <= first_hit:
            i += 1
            first_total += a[i]
            
        last_total = a[-1]

        j = -1

        while last_total <= last_hit:
            j -= 1
            last_total += a[j]
        
        print(i+-j - 1)