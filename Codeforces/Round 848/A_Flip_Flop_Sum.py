for tc in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))

    current_total = sum(array)

    arrays = []

    for i in range(len(array)-1):
        if [array[i], array[i+1]] == [1, 1]:
            arrays.append([array[i], array[i+1]])
        elif [array[i], array[i+1]] == [1, -1]:
            arrays.append([array[i], array[i+1]])
        elif [array[i], array[i+1]] == [-1, 1]:
            arrays.append([array[i], array[i+1]])
        else:
            arrays.append([-1, -1])
    
    if [-1, -1] in arrays:
        print(current_total+4)
    elif [-1, 1] in arrays or [1, -1] in arrays:
        print(current_total)
    else:
        print(current_total-4)