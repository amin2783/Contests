c = 'codeforces'

for tc in range(int(input())):
    s = input()

    difference = 0 

    for i in range(len(s)):
        if c[i]!=s[i]:
            difference+=1
    
    print(difference)