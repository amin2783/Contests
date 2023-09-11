for tc in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    sorted_arr = sorted(arr, reverse=True)
    d = dict()
    for i in range(1, n+1):
        if sorted_arr[i-1] in d:
            d[sorted_arr[i-1]] = [d[sorted_arr[i-1]]]
            d[sorted_arr[i-1]].append(i)
        else:
            d[sorted_arr[i-1]]=i
    
    for element in arr:
        if type(d[element]) == list:
            print(d[element].pop(0), end=' ')
        else:
            print(d[element], end=' ')
    
    print()

    
    # print(diff)