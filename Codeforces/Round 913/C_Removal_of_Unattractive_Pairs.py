for tc in range(int(input())):
    n = int(input())
    s = input()

    n = 0

    while len(s) >= 2 and n < (len(s) - 1):
        if s[n] != s[n+1]:
            s = s[:n] + s[n+2:]
            n = 0
        else:
            n += 1
    
    print(len(s))