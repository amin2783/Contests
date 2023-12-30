line = ''

for tc in range(int(input())):
    l1 = input()
    if "?" in l1:
        line = l1
    l2 = input()
    if "?" in l2:
        line = l2
    l3 = input()
    if "?" in l3:
        line = l3

    if "A" not in line:
        print("A")
    elif "B" not in line:
        print("B")
    else:
        print("C")