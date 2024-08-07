for tc in range(int(input())):
    s = (input())
    t = (input())
    count = s.count("?")

    if count > len(t):
        print(f"{''.join(t)}{'a'*(count-len(t))}")
    elif count == len(t):
        print(''.join(t))
    else:
        diff = abs(count-len(t)):
        t = set(t)
        while True:
            for 
