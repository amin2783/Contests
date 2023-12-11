for tc in range(int(input())):
    keypresses = list(input())



    n = 0 
    uppers = []
    lowers = []

    while n<len(keypresses):
        if keypresses[n] == "B":
            keypresses[n] = ""
            if len(uppers):
                keypresses[uppers.pop()] = ""
            #     n -= 2
            # else:
            #     n -= 1
        elif keypresses[n] == "b":
            keypresses[n] = ""
            if len(lowers):
                keypresses[lowers.pop()] = ""
            #     n -= 2
            # else:
            #     n -= 1
        else:
            if keypresses[n].isupper():
                uppers.append(n)
            else:
                lowers.append(n)
        
        n += 1
    
    print(''.join(keypresses))









    # uppers = []
    # lowers = []

    # deletions = []
    
    # n = 0

    # for keypress in keypresses:
    #     if keypress == "b":
    #         deletions.append(n)
    #         if len(lowers):
    #             deletions.append(lowers.pop())
                
    #     elif keypress == "B":
    #         deletions.append(n)
    #         if len(uppers):
    #             deletions.append(uppers.pop())
                
    #     else:
    #         if keypress.isupper():
    #             uppers.append(n)
    #         else:
    #             lowers.append(n)
    #     n += 1
    
    # s = list(keypresses)

    # deletions.sort(reverse=True)

    # for deletion in deletions:
    #     del s[deletion]
    
    # print(''.join(s))