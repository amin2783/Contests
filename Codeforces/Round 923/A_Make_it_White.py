def func(n, arr):
    for left in range(n):
        if arr[left] == "B":
            left_stop = left
            break
    if left == n-1:
        left_stop = left
        right_stop = left + 1

    
    for right in reversed(range(left_stop, n)):
        if arr[right] == "B":
            right_stop = right
            break
    
    return(right_stop-left_stop+1)

for tc in range(int(input())):

    n = int(input())
    arr = input()

    print(func(n, arr))


    # for left in range(n):
    #     if arr[left] == "B":
    #         left_stop = left
    #         break
    # if left == n-1:
    #     left_stop = left
    #     right_stop = left + 1

    
    # for right in reversed(range(n, left_stop)):
    #     if arr[right] == "B":
    #         right_stop = right
    #         break
    
    
    # print(right_stop-left_stop)