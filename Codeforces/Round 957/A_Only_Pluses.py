for tc in range(int(input())):
    b = list(map(int, input().split()))
    for i in range(5):
        b.sort()
        b[0] += 1
    
    print(b[0]*b[1]*b[2])