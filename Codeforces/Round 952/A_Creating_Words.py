for tc in range(int(input())):
    a, b = input().split()

    a_new = b[0] + a[1:]
    b_new = a[0] + b[1:]

    print(a_new, b_new)