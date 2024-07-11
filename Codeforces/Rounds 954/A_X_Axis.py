for tc in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()

    print(abs(a[2]-a[0]))