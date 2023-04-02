for tc in range(int(input())):
    a, b, c, d = map(int, input().split())

    if d < b:
        print(-1)
    elif (d-b) < (c-a):
        print(-1)
    else:
        a += (d-b)
        print((d-b) + (a-c))