def is_C(letter):
    if letter == "a" or letter == "e":
        return False
    return True

def is_odd(num):
    if num%2 == 0:
        return False
    return True



for tc in range(int(input())):
    n = int(input())
    letters = list(input())

    i = 0
    left = n

    while left > 4:
        if not is_C(letters[i+3]):
            letters[i+1] = letters[i+1]+"."
            i += 2
            left -= 2
        else:
            letters[i+2] = letters[i+2]+"."
            i += 3
            left -= 3
    
    if not is_odd(left):
        if left != 2:
            letters[i+1] = letters[i+1]+"."

    print(''.join(letters))


    