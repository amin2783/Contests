for tc in range(int(input())):

    n = int(input())
    s = input()

    while True:
        if s[0] == '0' and s[-1] == '1':
            s = s[1:]
            s = s[:-1]
            if s == '':
                break
        elif s[0] == '1' and s[-1] == '0':
            s = s[1:]
            s = s[:-1]
            if s == '':
                break
        else:
            break
    
    print(len(s))