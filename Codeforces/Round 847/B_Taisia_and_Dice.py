for tc in range(int(input())):
    n, s, r = map(int, input().split())

    soln = [s-r]
    n -= 1
    s -= s-r

    while n!=0:
        if s%n!=0:
            soln.append(s//n)
            s -= s//n
            n -= 1
        else:
            soln.extend(([s//n]*n))
            break
    
    for face in soln:
        print(face, end=' ')
    print()