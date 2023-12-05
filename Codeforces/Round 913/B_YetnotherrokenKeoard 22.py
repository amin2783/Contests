for tc in range(int(input())):
    keypresses = list(input())

    uppers = []
    lowers = []
    
    n = 0

    for keypress in keypresses:
        if keypress == "b":
            if len(lowers):
                del lowers[-1]
        elif keypress == "B":
            if len(uppers):
                del uppers[-1]
        else:
            if keypress.isupper():
                uppers.append(n)
            else:
                lowers.append(n)
        n += 1

    t = uppers+lowers
    t.sort()

    output = ''
    for index in t:
        output += keypresses[index]
    
    print(output)