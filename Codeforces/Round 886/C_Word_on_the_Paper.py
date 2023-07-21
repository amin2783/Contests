for tc in range(int(input())):
    letters = []
    for i in range(8):
        for letter in input():
            if letter == ".":
                pass
            else:
                letters.append(letter)
    print(''.join(letters))