for tc in range(int(input())):
    numbers = list(map(int,input().split()))
    numbers.sort()

    if numbers[1] + numbers[2] >= 10:
        print("YES")
    else:
        print("NO")