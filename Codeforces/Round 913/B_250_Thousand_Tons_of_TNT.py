from math import floor

for tc in range(int(input())):
    n = int(input())
    weights = list(map(int, input().split()))
    weights.sort()

    i = n

    current_max_diff = abs(sum(weights[-int(floor(n//i)):]) - sum(weights[:int(floor(n//i))]))

    i-=1

    while i > 0:
        if abs((sum(weights[-int(floor(n//i)):]) - sum(weights[:int(floor(n//i))]))) < current_max_diff:
            pass
        else:
            current_max_diff = abs(sum(weights[-int(floor(n//i)):]) - sum(weights[:int(floor(n//i))]))
        
        i-=1
    
    print(current_max_diff)
        