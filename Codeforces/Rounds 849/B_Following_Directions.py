for tc in range(int(input())):

    position = [0,0]

    n = int(input())
    moves = input()

    for move in range(n):
        if moves[move] == "L":
            position[0] -= 1
            if position == [1, 1]:
                print("YES")
                break 
        elif moves[move] == "R":
            position[0] += 1
            if position == [1, 1]:
                print("YES")
                break 
        elif moves[move] == "U":
            position[1] += 1
            if position == [1, 1]:
                print("YES")
                break 
        else:
            position[1] -= 1
            if position == [1, 1]:
                print("YES")
                break
        
    if move == n-1 and position != [1, 1]:
        print("NO")
        


