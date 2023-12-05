rows = [1, 2, 3, 4, 5, 6, 7, 8]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]


for tc in range(int(input())):
    inp = input()
    c, r = inp[0], int(inp[1])
    for column in columns:
        if column != c:
            print(f'{column}{r}')
    for row in rows:
        if row != r:
            print(f'{c}{row}') 