def factors(l):
    d = {1:0}
    for i in range(2, l):
        if l%i == 0:
            d[i] =0
    return d


def coins(fact):
    coins = fact + 4 + (2*((l-fact)//fact))
    return coins



for tc in range(int(input())):
    l = int(input())

    if l <= 4:
        coin = l
    else:
        facts = factors(l)
        print(factors(l))
        t = [coins(fact) for fact in facts]
        t.append(l)
        print(t)
        coin = sorted(t)[0]
    
    print(f'Case #{tc+1}: {coin}')
