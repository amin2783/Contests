pattern = "FBFFBFFBFBFFBFFBFBFFBFFBFBFFBFFBFBFFBFFBFBFFBFFB"

for tc in range(int(input())):
    k = int(input())
    s = input()

    if s in pattern:
        print("YES")
    else:
        print("NO")