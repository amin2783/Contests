for tc in range(int(input())):
    n = int(input())

    qualities = []
    for i in range(n):
        a, b = map(int, input().split())
        qualities.append((b, a))
    
    #print("\n",qualities,"\n")
    
    sorted_qualities = sorted(qualities, reverse=True)
    #print("\n",sorted_qualities,"\n")

    for participant in sorted_qualities:
        if participant[1] <= 10:
            break
    
    index = 1
    for element in qualities:
        if element == participant:
            print(index)
            break
        else:
            index+=1