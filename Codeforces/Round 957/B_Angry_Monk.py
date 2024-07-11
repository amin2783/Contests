for tc in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    operations = 0

    for piece in range(k-1):
        if a[piece] == 1:
            operations += 1
        else:
            operations += (2*a[piece] )-1

    print(operations)