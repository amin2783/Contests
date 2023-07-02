for tc in range(int(input())):
    l, n = map(int, input().split())

    #first run
    di, dir_i = input().split()
    di = int(di)

    count = di//l
    d = di%l
    dir = dir_i 

    #consecutive runs
    for run in range(1, n):
        di, dir_i = input().split()
        di = int(di)
        
        if dir_i == dir:
            count += (d+di)//l
            d = (d+di)%l
            
        else:
            if di >= d:
                di = di - d
                count += di//l
                d = di%l
                dir = dir_i
            else:
                d = d - di
            
            
    
    print(f'Case #{tc+1}: {count}')