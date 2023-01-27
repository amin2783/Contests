def histogram(s):
    d = dict()

    for lisst in s:
        for c in lisst:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def frequency(s):
    return invert_dict(histogram(s))


for tc in range(int(input())):
    n = int(input())

    sequences = []

    for i in range(n):
        sequences.append(list(map(int, input().split())))
    
    print(histogram(sequences))