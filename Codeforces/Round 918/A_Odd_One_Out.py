for tc in range(int(input())):
    t = list(map(int, input().split()))
    t.sort()

    if t[0]==t[1]:
        print(t[2])
    else:
        print(t[0])
    