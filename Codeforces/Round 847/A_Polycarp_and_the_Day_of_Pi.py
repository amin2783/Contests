pi = '314159265358979323846264338327950288'



for tc in range(int(input())):
    n = input()

    correct = 0 

    for i in range(len(n)):
        if pi[i] == n[i]:
            correct += 1
        else:
            break
    
    print(correct)