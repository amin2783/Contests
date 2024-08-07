for tc in range(int(input())):
    n, s, m = map(int, input().split())
    intervals = []

    for interval in range(n):
        intervals.append(list(map(int, input().split())))

    previous_end = 0
    next_start = intervals[0][0]

    for i in range(n):
        if (-previous_end + intervals[i][0]) >= s:
            print("YES")
            break
        else:
            previous_end = intervals[i][1]
    
    else:
        if (-previous_end + m) >= s:
            print("YES")
        else:
            print("NO")