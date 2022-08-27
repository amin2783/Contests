for tc in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))

    prev_max = v[0]
    records = 0

    if n > 1:
        if v[0] > v[1]:
            records += 1
            prev_max = v[1]

        for i in range(1, n-1):
            if v[i+1] < v[i] and v[i] > prev_max:
                records += 1
                prev_max = v[i]
        
        if v[n-1] > prev_max:
                records += 1
    else:
        if v[0] > 0:
            records = 1
        else:
            records = 0
    print(f'Case #{tc+1}: {records}')