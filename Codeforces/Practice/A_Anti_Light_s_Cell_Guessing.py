for tc in range(int(input())):
    n, m = map(int, input().split())
    
    if m==1 and n==1:
        print(0)
    elif m==1 or n==1:
        print(1)
    else:
        print(2)