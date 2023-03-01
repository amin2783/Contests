s = []

for i in range(1, 999):
    if i%3==0 and i%5==0:
        s.append('FB')
    elif i%3==0:
        s.append('F')
    elif i%5==0:
        s.append('B')

print(''.join(s))