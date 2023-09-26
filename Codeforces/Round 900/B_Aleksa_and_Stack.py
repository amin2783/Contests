for tc in range(int(input())):
    n = int(input())

    current_max = 5
    arr = [2,3,4]

    appendix = [0]*(n-3)

    arr.extend(appendix)

    for i in range(1, n-2):
        arr[i+2] = current_max
        while ((3*arr[i+2])%(arr[i]+arr[i+1]))==0:
            current_max += 1
            arr[i+2] = current_max
        current_max += 1
    
    print(*arr, sep = ' ')