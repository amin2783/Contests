for tc in range(int(input())):

    lst = []

    for n in range(int(input())):
        di, si = map(int, input().split())
        lst.append((di,si))
    
    lst.sort()

    d1, s1 = lst[0]

    max = (d1 + ((s1-1)//2))

    for (di, si) in lst:
        if (di + ((si-1)//2)) < max:
            max = (di + ((si-1)//2))
            # break
        # else:
        #     max = (di + ((si-1)//2))
        #     break
    
    print(max)