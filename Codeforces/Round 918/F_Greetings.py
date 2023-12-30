for tc in range(int(input())):
    n = int(input())
    t = []
    # d = dict()
    # ends = []
    for _ in range(n):
        a = tuple(map(int, input().split()))
        t.append(a)
        # ends.append(a[1])

    
    t.sort()
    # ends.sort()

    # d = dict()
    total = 0
    


    i = 1
    for start, end in t:
        j = i
        while j < n:
            startt, endd = t[j]
            if startt>start and endd<=end:
                total += 1
            j+=1
        i+=1

    # i = 0
    # for end in ends:
    #     d[end] = i
    #     i+=1
    

    
    # for person in t:
    #     start, end = person
    #     while d.get(start, "nonexistent") == "nonexistent":
    #         start += 1
    #     diff = (ends.index(end) - ends.index(start)) 
    #     count += diff
    #     del d[end]
    #     ends.remove(end)
    
    print(total)

        