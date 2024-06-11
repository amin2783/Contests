for tc in range(int(input())):
    n, m = map(int, input().split())
    
    ordinate_found = False
    old_r = []

    pounds = 0

    for row in range(n):
        r = list(input())
        if (max(pounds, r.count("#")) > r.count("#")) and ordinate_found == False :
            ordinate = row 
            ordinate_found = True
            abscissa = ((old_r.count("#"))//2) + old_r.index("#")
        elif row == n-1 and r.count("#")==1 and pounds == 0:
            ordinate = row+1
            abscissa = r.index("#")
            

        pounds = r.count("#")
        old_r = r

    print(ordinate, abscissa+1)