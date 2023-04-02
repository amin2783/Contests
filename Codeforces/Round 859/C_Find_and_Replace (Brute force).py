for tc in range(int(input())):
    n = int(input())
    s = input()

    flag = True

    for i in range(0, n, 2):
        temp = []
        if i+1 <= n:
            for j in range(i+1, n, 2):
                temp.append(s[j])
            if s[i] in temp:
                print("NO")
                flag = False
                break

    if flag:
        for i in range(1, n, 2):
            temp = []
            if i+1 <= n:
                for j in range(i+1, n, 2):
                    temp.append(s[j])
                if s[i] in temp:
                    print("NO")
                    flag = False
                    break
    
    if flag:
        print("YES")