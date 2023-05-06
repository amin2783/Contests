for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max = 0

    current = 1
    if n == 1:
        if arr[0] == 0:
            max = 1
    else:
        for i in range(n-1):
            if arr[i] == 0:
                if max == 0:
                    max += 1
                if arr[i]==arr[i+1]:
                    current+=1
                else:
                    if current > max:
                        max = current
                    current = 1 
    print(max)