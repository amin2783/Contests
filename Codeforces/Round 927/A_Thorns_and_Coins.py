for tc in range(int(input())):
    n = int(input())
    s = input()

    coins  = 0

    for idx in range(1, n):
        if s[idx] == "@":
            coins += 1
        
        if s[idx-1]=="*" and s[idx]== "*":
            break

            
    print(coins)