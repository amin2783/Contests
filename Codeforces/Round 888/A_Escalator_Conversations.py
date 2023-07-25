for tc in range(int(input())):
    n, m, k, H = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()

    # differences = []

    # i = 0 
    # while h[i]-H <= 0 and i<len(h):
    #     differences.append(H-h[i])
    #     i+=1
    # while i<len(h):
    #     differences.append()

    differences = [abs((h[i]-H)) for i in range(len(h))]


    # print(differences)
    persons = 0

    for difference in differences:
        # if difference >= 0:
        if difference%k == 0 and difference!=0:
            if difference//k < m:
                persons += 1
    
    print(persons)