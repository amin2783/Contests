for tc in range(int(input())):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()
    a = b[0]

    arr = []
    for col in range(n):
        for row in range(n):
            arr.append(a + (col*c) + (row*d))
    
    arr.sort()



    if arr==b:
        print("YES")
    else:
        print("NO")


