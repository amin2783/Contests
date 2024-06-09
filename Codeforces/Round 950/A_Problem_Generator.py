for tc in range(int(input())):
    n, m = map(int, input().split())
    a = input()

    d = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0}

    for difficulty in a:
        d[difficulty] += 1
    
    new = 0

    for value in d.values():
        if value < m:
            new += m - value

    print(new)