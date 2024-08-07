for tc in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    wins = 0

    if a1 >= b1:
        if a1 == b1:
            if a2 > b2:
                wins += 2
        else:
            if a2 >= b2:
                wins += 2
    if a1 >= b2:
        if a1 == b2:
            if a2 > b1:
                wins += 2
        else:
            if a2 >= b1:
                wins += 2
    
    print(wins)