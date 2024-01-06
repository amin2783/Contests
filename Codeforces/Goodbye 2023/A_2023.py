for tc in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))

    t = []
    product = 1

    for number in b:
        product *= number
    
    if 2023%product != 0:
        print("NO")
    else:
        t.append(str(2023//product))
        k-=1
        while k > 0:
            t.append(str(1))
            k-=1
        print("YES")
        print(' '.join(t))
