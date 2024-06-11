for tc in range(int(input())):
    a, b, n = map(int, input().split())
    tools = list(map(int, input().split()))

    total = b
    
    for tool in tools:
        if tool < a:
            total += tool
        else:
            total += a - 1
    
    print(total)