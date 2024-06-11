for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    good = 0

    for j in range(n):
        prefix = a[:j+1]
        # if prefix == [0]:
        #     good += 1
        if sum(prefix) == 2*max(prefix):
            good += 1            

    print(good)

