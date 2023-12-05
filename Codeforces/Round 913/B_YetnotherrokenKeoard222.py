for tc in range(int(input())):
    keypresses = list(input())

    uppers = []
    lowers = []

    deletions = dict()
    
    n = 0

    for keypress in keypresses:
        if keypress == "b":
            deletions.append(n)
            if len(lowers):
                deletions.append(lowers.pop())
                
        elif keypress == "B":
            deletions.append(n)
            if len(uppers):
                deletions.append(uppers.pop())
                
        else:
            if keypress.isupper():
                uppers.append(n)
            else:
                lowers.append(n)
        n += 1
    
    

    deletions.sort(reverse=True)

    for deletion in deletions:
        del s[deletion]
    
    print(''.join(s))