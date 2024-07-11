for tc in range(int(input())):
    n, m = map(int, input().split())

    arr = []
    for row in range(n):
        arr.append(list(map(int, input().split())))


    if n==1 and m==1:
        print(arr)
    
    
    elif n == 1 and m != 1:
        for r in range(n):
            for c in range(m):
                if c == 0:
                    if arr[r][c] > arr[r][c+1]:
                        arr[r][c] = arr[r][c+1]
                        print(arr[r][c], end=' ')
                    else:
                        print(arr[r][c], end=' ')
                elif c == m-1:
                    if arr[r][c] > arr[r][c-1]:
                        arr[r][c] = arr[r][c-1]
                        print(arr[r][c], end='\n')
                    else:
                        print(arr[r][c], end='\n')
                else:
                    if arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1]:
                        arr[r][c] = max(arr[r][c+1], arr[r][c-1])
                        print(arr[r][c], end=' ')
                    else:
                        print(arr[r][c], end=' ')
                
    
    elif m == 1 and n != 1:
        for r in range(n):
            for c in range(m):
                if r == 0:
                    if arr[r][c] > arr[r+1][c]:
                        arr[r][c] = arr[r+1][c]
                        print(arr[r][c], end='\n')
                    else:
                        print(arr[r][c], end='\n')
                    
                elif r == n-1:
                    if arr[r][c] > arr[r-1][c]:
                        arr[r][c] = arr[r-1][c]
                        print(arr[r][c], end='\n')
                    else:
                        print(arr[r][c], end='\n')
                    
                
                else:
                    if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r-1][c]:
                        arr[r][c] = max(arr[r+1][c], arr[r-1][c])
                        print(arr[r][c], end='\n')
                    else:
                        print(arr[r][c], end='\n')

    else:
        for r in range(n):
            for c in range(m):
                if r == 0:
                    if c == 0:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c+1])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')
                    elif c == m-1:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c-1]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c-1])
                            print(arr[r][c], end='\n')
                        else:
                            print(arr[r][c], end='\n')
                    else:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r][c-1])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')
                
                elif r == n-1:
                    if c == 0:
                        if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c+1]:
                            arr[r][c] = max(arr[r-1][c], arr[r][c+1])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')
                    elif c == m-1:
                        if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c-1]:
                            arr[r][c] = max(arr[r-1][c], arr[r][c-1])
                            print(arr[r][c], end='\n')
                        else:
                            print(arr[r][c], end='\n')
                    else:
                        if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1]:
                            arr[r][c] = max(arr[r-1][c], arr[r][c+1], arr[r][c-1])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')
                
                else:
                    if c == 0:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r-1][c]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r-1][c])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')
                    elif c == m-1:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c-1] and arr[r][c] > arr[r-1][c]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c-1], arr[r-1][c])
                            print(arr[r][c], end='\n')
                        else:
                            print(arr[r][c], end='\n')
                    else:
                        if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1] and arr[r][c] > arr[r-1][c]:
                            arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r][c-1], arr[r-1][c])
                            print(arr[r][c], end=' ')
                        else:
                            print(arr[r][c], end=' ')












    # for r in range(n):
    #     for c in range(m):
    #         if r == 0:
    #             if c == 0:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c+1])
    #                     print(arr[r][c], end=' ')
    #                 #no else
    #             elif c == m-1:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c-1]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c-1])
    #                     print(arr[r][c], end='\n')
    #                 #no else
    #             else:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r][c-1])
    #                     print(arr[r][c], end=' ')
    #                 #no else
            
    #         elif r == n-1:
    #             if c == 0:
    #                 if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c+1]:
    #                     arr[r][c] = max(arr[r-1][c], arr[r][c+1])
    #                     print(arr[r][c], end=' ')
    #                 #no else
    #             elif c == m-1:
    #                 if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c-1]:
    #                     arr[r][c] = max(arr[r-1][c], arr[r][c-1])
    #                     print(arr[r][c], end='\n')
    #                 #no else
    #             else:
    #                 if arr[r][c] > arr[r-1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1]:
    #                     arr[r][c] = max(arr[r-1][c], arr[r][c+1], arr[r][c-1])
    #                     print(arr[r][c], end=' ')
    #                 #no else
            
    #         else:
    #             if c == 0:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r-1][c]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r-1][c])
    #                     print(arr[r][c], end=' ')
    #                 #no else
    #             elif c == m-1:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c-1] and arr[r][c] > arr[r-1][c]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c-1], arr[r-1][c])
    #                     print(arr[r][c], end='\n')
    #                 #no else
    #             else:
    #                 if arr[r][c] > arr[r+1][c] and arr[r][c] > arr[r][c+1] and arr[r][c] > arr[r][c-1] and arr[r][c] > arr[r-1][c]:
    #                     arr[r][c] = max(arr[r+1][c], arr[r][c+1], arr[r][c-1], arr[r-1][c])
    #                     print(arr[r][c], end=' ')
    #                 #no else

