for tc in range(int(input())):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    print(f'Case #{tc+1}: {sum(c)%m}')
