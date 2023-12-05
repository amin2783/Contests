for tc in range(int(input())):
    keypresses = list(input())

    d = dict()

    uppers = []
    lowers = []

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